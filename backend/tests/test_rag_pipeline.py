import os
import io
import fitz
import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import get_db, init_db
from app.services.rag_service import rag_service, EmptyPDFError, InvalidPDFError

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_test_db():
    init_db()
    yield

def create_synthetic_pdf(pages_text: list[str]) -> bytes:
    """Creates a real in-memory PDF using PyMuPDF (fitz) with text on each page."""
    doc = fitz.open()
    for text in pages_text:
        page = doc.new_page()
        if text:
            page.insert_textbox(fitz.Rect(50, 50, 550, 750), text)
    pdf_bytes = doc.tobytes()
    doc.close()
    return pdf_bytes


# --------------------------------------------------------------------------
# 1. Upload Validation Tests
# --------------------------------------------------------------------------
def test_upload_rejects_non_pdf_extension():
    response = client.post(
        "/api/documents/upload",
        files={"file": ("notes.txt", b"Some text content", "text/plain")}
    )
    assert response.status_code == 400
    assert "Only PDF files (.pdf) are supported" in response.json()["detail"]

def test_upload_rejects_empty_file():
    response = client.post(
        "/api/documents/upload",
        files={"file": ("empty.pdf", b"", "application/pdf")}
    )
    assert response.status_code == 400
    assert "empty" in response.json()["detail"].lower()

def test_upload_rejects_invalid_pdf_header():
    response = client.post(
        "/api/documents/upload",
        files={"file": ("corrupt.pdf", b"This is not a real PDF file content", "application/pdf")}
    )
    assert response.status_code == 400
    assert "signature" in response.json()["detail"].lower() or "invalid" in response.json()["detail"].lower()


# --------------------------------------------------------------------------
# 2. PyMuPDF Extraction and Page Metadata Tests
# --------------------------------------------------------------------------
def test_extract_text_and_page_metadata(tmp_path):
    pdf_bytes = create_synthetic_pdf([
        "Page 1: Time and Work fundamentals. If A takes 10 days and B takes 15 days, together they take 6 days.",
        "Page 2: Percentage formulas. Percentage change = (Change / Original) * 100."
    ])
    temp_file = tmp_path / "test_extract.pdf"
    temp_file.write_bytes(pdf_bytes)

    pages_data = rag_service.extract_text_from_pdf(str(temp_file))
    assert len(pages_data) == 2
    assert pages_data[0][0] == 1
    assert "Time and Work fundamentals" in pages_data[0][1]
    assert pages_data[1][0] == 2
    assert "Percentage formulas" in pages_data[1][1]


# --------------------------------------------------------------------------
# 3. Empty or Scanned PDF Handling
# --------------------------------------------------------------------------
def test_upload_rejects_empty_or_scanned_pdf_with_no_extractable_text():
    # Synthetic PDF with blank pages (simulating image/scanned PDF without OCR)
    blank_pdf_bytes = create_synthetic_pdf(["", ""])
    response = client.post(
        "/api/documents/upload",
        files={"file": ("scanned_blank.pdf", blank_pdf_bytes, "application/pdf")}
    )
    assert response.status_code == 422
    assert "ocr" in response.json()["detail"].lower()

    # Verify that failed upload cleaned up DB record and did not leave zombie rows
    docs_res = client.get("/api/documents")
    assert docs_res.status_code == 200
    doc_names = [d["original_name"] for d in docs_res.json()["documents"]]
    assert "scanned_blank.pdf" not in doc_names

    # Verify no orphaned file left in documents directory
    assert not any("scanned_blank.pdf" in f for f in os.listdir(rag_service.documents_dir))


# --------------------------------------------------------------------------
# 4. Chunking and Metadata Preservation
# --------------------------------------------------------------------------
def test_chunking_preserves_page_numbers_and_metadata():
    pages = [
        (1, "Aptitude Section 1. Work done per day is reciprocal of total days. " * 8),
        (2, "Aptitude Section 2. Speed equals distance divided by time. " * 8)
    ]
    chunks = rag_service.chunk_pages_data(pages, "doc_test123", "StudyGuide.pdf")

    assert len(chunks) >= 2
    for c in chunks:
        assert c["document_id"] == "doc_test123"
        assert c["document_name"] == "StudyGuide.pdf"
        assert c["page_number"] in [1, 2]
        assert "chunk_index" in c
        assert len(c["text"]) > 30


# --------------------------------------------------------------------------
# 5. Full Document Lifecycle, Retrieval Isolation, and Deletion
# --------------------------------------------------------------------------
def test_document_upload_retrieval_isolation_and_deletion():
    # Create Document A (Time and Work)
    doc_a_bytes = create_synthetic_pdf([
        "Quantitative Aptitude - Pipes and Cisterns. Pipe A fills in 12 hours, Pipe B fills in 18 hours. Net efficiency is 5/36 per hour."
    ])
    # Create Document B (Verbal Ability)
    doc_b_bytes = create_synthetic_pdf([
        "Verbal Comprehension - Reading Passage on Artificial Intelligence and Economics. Vocabulary synonyms: ephemeral means short-lived."
    ])

    # Upload Doc A
    res_a = client.post(
        "/api/documents/upload",
        files={"file": ("cisterns.pdf", doc_a_bytes, "application/pdf")}
    )
    assert res_a.status_code == 201
    doc_a_id = res_a.json()["id"]
    assert res_a.json()["status"] == "ready"
    assert res_a.json()["page_count"] == 1

    # Upload Doc B
    res_b = client.post(
        "/api/documents/upload",
        files={"file": ("verbal.pdf", doc_b_bytes, "application/pdf")}
    )
    assert res_b.status_code == 201
    doc_b_id = res_b.json()["id"]

    try:
        # Check list endpoint
        list_res = client.get("/api/documents")
        assert list_res.status_code == 200
        doc_ids = [d["id"] for d in list_res.json()["documents"]]
        assert doc_a_id in doc_ids
        assert doc_b_id in doc_ids

        # Test retrieval isolation: querying Doc A for 'ephemeral' should NOT find Doc B's content
        chunks_from_a = rag_service.retrieve_relevant_chunks(doc_a_id, "What does ephemeral mean?", top_k=3)
        for chunk in chunks_from_a:
            assert "Artificial Intelligence" not in chunk["text"]
            assert "ephemeral" not in chunk["text"]

        # Querying Doc B for 'ephemeral' should retrieve Doc B's content
        chunks_from_b = rag_service.retrieve_relevant_chunks(doc_b_id, "What does ephemeral mean?", top_k=3)
        assert any("ephemeral" in c["text"] for c in chunks_from_b)
        assert all(c["page"] == 1 for c in chunks_from_b)

    finally:
        # Cleanup Doc A & Doc B
        del_a = client.delete(f"/api/documents/{doc_a_id}")
        assert del_a.status_code == 200
        del_b = client.delete(f"/api/documents/{doc_b_id}")
        assert del_b.status_code == 200

        # Verify deletion from DB
        get_res = client.get(f"/api/documents/{doc_a_id}")
        assert get_res.status_code == 404

        # Verify Chroma vector cleanup
        remaining_chunks = rag_service.retrieve_relevant_chunks(doc_a_id, "test", top_k=1)
        assert len(remaining_chunks) == 0


# --------------------------------------------------------------------------
# 6. Missing Document Errors
# --------------------------------------------------------------------------
def test_missing_document_returns_404():
    res = client.get("/api/documents/non_existent_doc_123")
    assert res.status_code == 404

    res = client.delete("/api/documents/non_existent_doc_123")
    assert res.status_code == 404

    res = client.post(
        "/api/documents/non_existent_doc_123/ask",
        json={"question": "What is the formula?"}
    )
    assert res.status_code == 404


# --------------------------------------------------------------------------
# 7. Grounded PDF Q&A with Mocked LLM
# --------------------------------------------------------------------------
def test_document_ask_qa_grounded_with_mocked_llm():
    pdf_bytes = create_synthetic_pdf([
        "Profit and Loss Formula: Profit = Selling Price - Cost Price. Profit percentage = (Profit / Cost Price) * 100."
    ])
    upload_res = client.post(
        "/api/documents/upload",
        files={"file": ("profit_loss.pdf", pdf_bytes, "application/pdf")}
    )
    doc_id = upload_res.json()["id"]

    try:
        mock_choice = MagicMock()
        mock_choice.message.content = "Based on Page 1, Profit percentage is calculated as (Profit / Cost Price) * 100."
        mock_response = MagicMock(choices=[mock_choice])

        with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = mock_response
            mock_get_client.return_value = mock_client

            ask_res = client.post(
                f"/api/documents/{doc_id}/ask",
                json={"question": "How is profit percentage calculated?"}
            )

            assert ask_res.status_code == 200
            data = ask_res.json()
            assert "Profit percentage is calculated as" in data["answer"]
            assert data["document_id"] == doc_id
            assert data["document_name"] == "profit_loss.pdf"
            assert len(data["sources"]) > 0
            assert data["sources"][0]["page"] == 1
            assert "Selling Price - Cost Price" in data["sources"][0]["text"]

    finally:
        client.delete(f"/api/documents/{doc_id}")


# --------------------------------------------------------------------------
# 8. Grounded Question Generation Structure Validation with Mocked LLM
# --------------------------------------------------------------------------
def test_document_generate_questions_with_mocked_llm():
    pdf_bytes = create_synthetic_pdf([
        "Ratio and Proportion. If A:B = 2:3 and B:C = 4:5, then A:B:C = 8:12:15."
    ])
    upload_res = client.post(
        "/api/documents/upload",
        files={"file": ("ratios.pdf", pdf_bytes, "application/pdf")}
    )
    doc_id = upload_res.json()["id"]

    try:
        mock_json_content = """[
            {
                "question": "If A:B = 2:3 and B:C = 4:5, what is the combined ratio A:B:C?",
                "options": [
                    {"id": "A", "text": "8:12:15"},
                    {"id": "B", "text": "6:10:15"},
                    {"id": "C", "text": "8:10:12"},
                    {"id": "D", "text": "2:3:5"}
                ],
                "correct_option": "A",
                "explanation": "Multiply the first ratio by 4 and the second ratio by 3 to equate B: 2*4 : 3*4 : 5*3 = 8:12:15.",
                "source_pages": [1]
            }
        ]"""
        mock_choice = MagicMock()
        mock_choice.message.content = mock_json_content
        mock_response = MagicMock(choices=[mock_choice])

        with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
            mock_client = MagicMock()
            mock_client.chat.completions.create.return_value = mock_response
            mock_get_client.return_value = mock_client

            gen_res = client.post(
                f"/api/documents/{doc_id}/generate-questions",
                json={"topic": "Ratio and Proportion", "difficulty": "Medium", "count": 1}
            )

            assert gen_res.status_code == 200
            data = gen_res.json()
            assert data["document_id"] == doc_id
            assert len(data["questions"]) == 1
            q = data["questions"][0]
            assert q["question"] == "If A:B = 2:3 and B:C = 4:5, what is the combined ratio A:B:C?"
            assert len(q["options"]) == 4
            assert q["correct_option"] == "A"
            assert q["source_pages"] == [1]
            assert q["verified"] is True
            assert q["is_grounded"] is True

    finally:
        client.delete(f"/api/documents/{doc_id}")
