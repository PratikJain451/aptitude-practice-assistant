import os
import uuid
import logging
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from app.core.config import settings
from app.db.database import get_db
from app.schemas.api_models import (
    DocumentResponse,
    DocumentListResponse,
    DocumentAskRequest,
    DocumentAskResponse,
    GenerateQuestionsRequest,
    GenerateQuestionsResponse,
)
from app.services.rag_service import (
    rag_service,
    RAGException,
    DocumentNotFoundError,
    InvalidPDFError,
    EmptyPDFError,
    MAX_UPLOAD_SIZE,
)
from app.services.llm_service import (
    LLMConfigurationError,
    LLMAuthenticationError,
    LLMRateLimitError,
    LLMTimeoutError,
    LLMProviderError,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/documents", tags=["PDF Documents & RAG"])

@router.post("/upload", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(file: UploadFile = File(...)):
    """
    Uploads, validates, extracts text with PyMuPDF, chunks, embeds, and indexes a PDF document into ChromaDB.
    """
    original_filename = file.filename or "uploaded_document.pdf"

    # Extension check
    if not original_filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file format. Only PDF files (.pdf) are supported."
        )

    # Read file content safely
    try:
        content = await file.read()
    except Exception as e:
        logger.error("Failed to read uploaded file: %s", str(e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to read file from upload request."
        )

    file_size = len(content)

    # Content size validation
    if file_size == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The uploaded file is empty (0 bytes)."
        )

    if file_size > MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail=f"File exceeds maximum allowed size of 15 MB (size: {file_size / (1024 * 1024):.2f} MB)."
        )

    # Validate PDF signature
    if not content.startswith(b"%PDF-"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid PDF file. Header signature does not match PDF specification."
        )

    # Safe stored filename prevents path traversal
    doc_id = f"doc_{uuid.uuid4().hex[:12]}"
    safe_name = os.path.basename(original_filename)
    safe_stored_name = f"{doc_id}_{safe_name}"
    save_path = os.path.join(rag_service.documents_dir, safe_stored_name)

    # Save to disk
    try:
        with open(save_path, "wb") as f:
            f.write(content)
    except Exception as e:
        logger.error("Failed to write document to disk: %s", str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Could not store document on server filesystem."
        )

    # Record initial state in SQLite
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO documents (id, filename, original_name, file_size, page_count, chunk_count, status, error_message)
            VALUES (?, ?, ?, ?, 0, 0, 'uploaded', NULL)
        """, (doc_id, safe_stored_name, safe_name, file_size))

    # Process and index via PyMuPDF + SentenceTransformers + ChromaDB
    try:
        rag_service.process_and_index_document(doc_id)
    except EmptyPDFError as e:
        rag_service.cleanup_failed_upload(doc_id, safe_stored_name)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=e.message)
    except InvalidPDFError as e:
        rag_service.cleanup_failed_upload(doc_id, safe_stored_name)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except RAGException as e:
        rag_service.cleanup_failed_upload(doc_id, safe_stored_name)
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        rag_service.cleanup_failed_upload(doc_id, safe_stored_name)
        logger.error("Unexpected error processing document %s: %s", doc_id, str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Processing failed: {str(e)}")

    # Fetch final record
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents WHERE id = ?", (doc_id,))
        row = cursor.fetchone()

    return DocumentResponse(**dict(row))


@router.get("", response_model=DocumentListResponse)
def list_documents():
    """Lists all uploaded documents with processing status and page count."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents ORDER BY created_at DESC")
        rows = cursor.fetchall()
        documents = [DocumentResponse(**dict(r)) for r in rows]

    return DocumentListResponse(documents=documents, total=len(documents))


@router.get("/{document_id}", response_model=DocumentResponse)
def get_document(document_id: str):
    """Retrieves document metadata by ID."""
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM documents WHERE id = ?", (document_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Document '{document_id}' not found.")

    return DocumentResponse(**dict(row))


@router.delete("/{document_id}", status_code=status.HTTP_200_OK)
def delete_document(document_id: str):
    """Deletes document file, SQLite record, and associated vectors from ChromaDB."""
    try:
        rag_service.delete_document(document_id)
        return {"message": "Document and associated vectors deleted successfully.", "document_id": document_id}
    except DocumentNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Document '{document_id}' not found.")
    except Exception as e:
        logger.error("Error deleting document %s: %s", document_id, str(e))
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Deletion failed: {str(e)}")


@router.post("/{document_id}/ask", response_model=DocumentAskResponse)
def ask_document_doubt(document_id: str, request: DocumentAskRequest):
    """
    Grounded PDF Doubt Solving:
    Retrieves isolated chunks from the specified document and passes context to Groq LLM.
    """
    try:
        result = rag_service.ask_document(document_id, request.question)
        return DocumentAskResponse(**result)
    except DocumentNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    except LLMConfigurationError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=e.message)
    except LLMAuthenticationError as e:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=e.message)
    except LLMRateLimitError as e:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=e.message)
    except LLMTimeoutError as e:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail=e.message)
    except (LLMProviderError, RAGException) as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        logger.error("Error answering question on document %s: %s", document_id, str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to answer question.")


@router.post("/{document_id}/generate-questions", response_model=GenerateQuestionsResponse)
def generate_questions_from_document(document_id: str, request: GenerateQuestionsRequest):
    """
    Grounded Aptitude Question Generation:
    Generates multiple-choice practice questions grounded in the PDF's content.
    """
    try:
        result = rag_service.generate_questions(
            document_id=document_id,
            topic=request.topic,
            difficulty=request.difficulty,
            count=request.count
        )
        return GenerateQuestionsResponse(**result)
    except DocumentNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.message)
    except LLMConfigurationError as e:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=e.message)
    except LLMAuthenticationError as e:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=e.message)
    except LLMRateLimitError as e:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=e.message)
    except LLMTimeoutError as e:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail=e.message)
    except (LLMProviderError, RAGException) as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        logger.error("Error generating questions from document %s: %s", document_id, str(e), exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to generate questions.")
