import os
import re
import uuid
import logging
from typing import List, Dict, Any, Optional, Tuple
import fitz  # PyMuPDF
from app.core.config import settings
from app.db.database import get_db
from app.services.llm_service import llm_service, LLMServiceException

logger = logging.getLogger(__name__)

# Constants
MAX_CHUNK_CHAR_SIZE = 650
MIN_CHUNK_CHAR_SIZE = 150
CHUNK_OVERLAP = 90
MAX_UPLOAD_SIZE = settings.MAX_FILE_SIZE_BYTES  # 15 MB

class RAGException(Exception):
    """Base exception for RAG pipeline errors."""
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class DocumentNotFoundError(RAGException):
    def __init__(self, document_id: str):
        super().__init__(f"Document with ID '{document_id}' was not found.", status_code=404)

class InvalidPDFError(RAGException):
    def __init__(self, message: str):
        super().__init__(message, status_code=400)

class EmptyPDFError(RAGException):
    def __init__(self, message: str = "No extractable text found in this PDF. Scanned or image-only PDFs require OCR, which is not supported in this milestone. Please upload a PDF with selectable text."):
        super().__init__(message, status_code=422)


class RAGService:
    def __init__(self):
        self._embedding_model = None
        self._chroma_client = None
        self._collection = None

        # Resolve storage paths
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.documents_dir = os.path.join(base_dir, settings.DOCUMENTS_DIR)
        self.chroma_dir = os.path.join(base_dir, settings.CHROMA_PERSIST_DIR)

        os.makedirs(self.documents_dir, exist_ok=True)
        os.makedirs(self.chroma_dir, exist_ok=True)

    @property
    def embedding_model(self):
        """Lazy singleton initialization of SentenceTransformer model."""
        if self._embedding_model is None:
            logger.info("Initializing SentenceTransformer with model %s...", settings.EMBEDDING_MODEL_NAME)
            from sentence_transformers import SentenceTransformer
            self._embedding_model = SentenceTransformer(settings.EMBEDDING_MODEL_NAME)
        return self._embedding_model

    @property
    def chroma_collection(self):
        """Lazy singleton initialization of persistent ChromaDB collection."""
        if self._collection is None:
            logger.info("Initializing ChromaDB PersistentClient at %s...", self.chroma_dir)
            import chromadb
            from chromadb.config import Settings as ChromaSettings
            self._chroma_client = chromadb.PersistentClient(
                path=self.chroma_dir,
                settings=ChromaSettings(anonymized_telemetry=False)
            )
            self._collection = self._chroma_client.get_or_create_collection(
                name="aptitude_rag_documents",
                metadata={"hnsw:space": "cosine"}
            )
        return self._collection

    # -------------------------------------------------------------
    # PDF Validation & Text Extraction
    # -------------------------------------------------------------
    def validate_pdf_bytes(self, file_bytes: bytes, filename: str) -> None:
        """Strict validation of PDF signature, size, and extension."""
        if not filename.lower().endswith(".pdf"):
            raise InvalidPDFError("Only files with .pdf extension are accepted.")

        if len(file_bytes) == 0:
            raise InvalidPDFError("Uploaded file is empty (0 bytes).")

        if len(file_bytes) > MAX_UPLOAD_SIZE:
            raise InvalidPDFError(f"File size exceeds the 15 MB limit ({len(file_bytes)} bytes).")

        # PDF header signature check
        if not file_bytes.startswith(b"%PDF-"):
            raise InvalidPDFError("Invalid PDF header signature. File does not appear to be a valid PDF.")

    def extract_text_from_pdf(self, file_path: str) -> List[Tuple[int, str]]:
        """
        Uses PyMuPDF (fitz) to extract text page by page.
        Returns a list of tuples: (page_number_1_indexed, page_text).
        Raises InvalidPDFError or EmptyPDFError on failures.
        """
        doc = None
        try:
            doc = fitz.open(file_path)
            if doc.is_encrypted:
                raise InvalidPDFError("Password-protected or encrypted PDFs are not supported. Please upload an unprotected PDF.")

            page_count = len(doc)
            if page_count == 0:
                raise InvalidPDFError("PDF has 0 pages.")

            pages_data: List[Tuple[int, str]] = []
            total_text_length = 0

            for page_index in range(page_count):
                page = doc[page_index]
                text = page.get_text() or ""
                # Normalize line breaks and tabs
                cleaned_text = re.sub(r"[ \t]+", " ", text).strip()
                pages_data.append((page_index + 1, cleaned_text))
                total_text_length += len(cleaned_text)

            if total_text_length == 0:
                raise EmptyPDFError()

            return pages_data

        except fitz.FileDataError as e:
            raise InvalidPDFError(f"Corrupt or unreadable PDF document: {str(e)}")
        except (InvalidPDFError, EmptyPDFError):
            raise
        except Exception as e:
            logger.error("PyMuPDF extraction failed: %s", str(e), exc_info=True)
            raise InvalidPDFError(f"Failed to read PDF document: {str(e)}")
        finally:
            if doc is not None:
                doc.close()

    # -------------------------------------------------------------
    # Chunking
    # -------------------------------------------------------------
    def chunk_pages_data(
        self,
        pages_data: List[Tuple[int, str]],
        document_id: str,
        document_name: str
    ) -> List[Dict[str, Any]]:
        """
        Splits text into chunks of 500-700 characters with 80-100 characters overlap,
        respecting sentence/paragraph boundaries while maintaining page metadata.
        """
        chunks: List[Dict[str, Any]] = []
        global_chunk_idx = 0

        for page_num, page_text in pages_data:
            if not page_text:
                continue

            # Split page text into sentences/paragraphs
            # First split by paragraphs
            paragraphs = [p.strip() for p in page_text.split("\n\n") if p.strip()]
            if not paragraphs:
                paragraphs = [page_text]

            current_chunk = ""
            for para in paragraphs:
                # If paragraph alone is longer than max chunk size, break by sentences
                if len(para) > MAX_CHUNK_CHAR_SIZE:
                    sentences = re.split(r"(?<=[.!?])\s+", para)
                else:
                    sentences = [para]

                for sentence in sentences:
                    sentence = sentence.strip()
                    if not sentence:
                        continue

                    if not current_chunk:
                        current_chunk = sentence
                    elif len(current_chunk) + len(sentence) + 1 <= MAX_CHUNK_CHAR_SIZE:
                        current_chunk += " " + sentence
                    else:
                        # Yield current chunk
                        if len(current_chunk) >= MIN_CHUNK_CHAR_SIZE:
                            chunks.append({
                                "id": f"{document_id}_p{page_num}_c{global_chunk_idx}",
                                "document_id": document_id,
                                "document_name": document_name,
                                "page_number": page_num,
                                "chunk_index": global_chunk_idx,
                                "text": current_chunk
                            })
                            global_chunk_idx += 1

                            # Overlap: keep tail of current chunk
                            tail = current_chunk[-CHUNK_OVERLAP:].strip() if len(current_chunk) > CHUNK_OVERLAP else ""
                            current_chunk = (tail + " " + sentence).strip()
                        else:
                            # If below min size, still append
                            current_chunk += " " + sentence

            if current_chunk and len(current_chunk.strip()) > 30:
                chunks.append({
                    "id": f"{document_id}_p{page_num}_c{global_chunk_idx}",
                    "document_id": document_id,
                    "document_name": document_name,
                    "page_number": page_num,
                    "chunk_index": global_chunk_idx,
                    "text": current_chunk.strip()
                })
                global_chunk_idx += 1

        return chunks

    # -------------------------------------------------------------
    # Document Ingestion Pipeline
    # -------------------------------------------------------------
    def process_and_index_document(self, document_id: str) -> Dict[str, Any]:
        """
        Executes full ingestion pipeline for an uploaded document:
        1. Fetch document record from DB.
        2. Extract text via PyMuPDF.
        3. Chunk text.
        4. Generate embeddings via BAAI/bge-small-en-v1.5.
        5. Persist vectors in ChromaDB.
        6. Update DB status to 'ready' (or 'failed' on error).
        """
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM documents WHERE id = ?", (document_id,))
            row = cursor.fetchone()
            if not row:
                raise DocumentNotFoundError(document_id)
            doc_record = dict(row)

        file_path = os.path.join(self.documents_dir, doc_record["filename"])
        if not os.path.exists(file_path):
            self._update_doc_status(document_id, "failed", "Physical document file missing on server.")
            raise RAGException("Physical document file missing on server.", status_code=500)

        try:
            self._update_doc_status(document_id, "processing")

            # Step 1: PyMuPDF Extraction
            pages_data = self.extract_text_from_pdf(file_path)
            page_count = len(pages_data)

            # Step 2: Chunking
            chunks = self.chunk_pages_data(pages_data, document_id, doc_record["original_name"])
            if not chunks:
                raise EmptyPDFError("Document produced no usable text chunks.")

            # Step 3: Embeddings
            texts = [c["text"] for c in chunks]
            embeddings = self.embedding_model.encode(texts, convert_to_numpy=True).tolist()

            # Step 4: Indexing in ChromaDB
            ids = [c["id"] for c in chunks]
            metadatas = [{
                "document_id": c["document_id"],
                "document_name": c["document_name"],
                "page_number": int(c["page_number"]),
                "chunk_index": int(c["chunk_index"])
            } for c in chunks]

            collection = self.chroma_collection
            # Clean up any existing vectors for this document first to avoid duplicates
            collection.delete(where={"document_id": document_id})
            collection.add(
                ids=ids,
                documents=texts,
                embeddings=embeddings,
                metadatas=metadatas
            )

            # Step 5: Update database record
            with get_db() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE documents
                    SET status = 'ready',
                        page_count = ?,
                        chunk_count = ?,
                        error_message = NULL,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (page_count, len(chunks), document_id))

            logger.info("Successfully processed document %s (%d pages, %d chunks).", document_id, page_count, len(chunks))
            return {
                "document_id": document_id,
                "status": "ready",
                "page_count": page_count,
                "chunk_count": len(chunks)
            }

        except (InvalidPDFError, EmptyPDFError) as e:
            logger.warning("Document %s processing rejected: %s", document_id, str(e))
            self._update_doc_status(document_id, "failed", e.message)
            raise
        except Exception as e:
            logger.error("Document %s processing failed with unexpected error: %s", document_id, str(e), exc_info=True)
            self._update_doc_status(document_id, "failed", f"Processing error: {str(e)}")
            raise RAGException(f"Failed to process document: {str(e)}", status_code=500)

    def _update_doc_status(self, document_id: str, status: str, error_message: Optional[str] = None):
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE documents
                SET status = ?, error_message = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            """, (status, error_message, document_id))

    # -------------------------------------------------------------
    # Document Deletion
    # -------------------------------------------------------------
    def delete_document(self, document_id: str) -> None:
        """Deletes document record, disk file, and associated ChromaDB vectors."""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT filename FROM documents WHERE id = ?", (document_id,))
            row = cursor.fetchone()
            if not row:
                raise DocumentNotFoundError(document_id)
            filename = row["filename"]

            # Remove from DB
            cursor.execute("DELETE FROM documents WHERE id = ?", (document_id,))

        # Remove from Chroma
        try:
            self.chroma_collection.delete(where={"document_id": document_id})
            logger.info("Deleted vectors for document %s from ChromaDB.", document_id)
        except Exception as e:
            logger.warning("Error deleting Chroma vectors for document %s: %s", document_id, str(e))

        # Remove file from disk
        file_path = os.path.join(self.documents_dir, filename)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                logger.info("Deleted physical file %s from disk.", file_path)
            except OSError as e:
                logger.warning("Could not delete file %s: %s", file_path, str(e))

    def cleanup_failed_upload(self, document_id: str, filename: Optional[str] = None) -> None:
        """Cleans up physical file, database record, and any vector store chunks after a failed upload."""
        logger.info("Cleaning up failed upload artifacts for document %s...", document_id)
        # 1. Remove database record
        try:
            with get_db() as conn:
                cursor = conn.cursor()
                if not filename:
                    cursor.execute("SELECT filename FROM documents WHERE id = ?", (document_id,))
                    row = cursor.fetchone()
                    if row:
                        filename = row["filename"]
                cursor.execute("DELETE FROM documents WHERE id = ?", (document_id,))
        except Exception as e:
            logger.warning("Failed to clean up DB record for %s: %s", document_id, str(e))

        # 2. Remove physical file
        if filename:
            file_path = os.path.join(self.documents_dir, filename)
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    logger.info("Removed failed upload file: %s", file_path)
                except OSError as e:
                    logger.warning("Failed to remove file %s: %s", file_path, str(e))

        # 3. Purge any vectors in Chroma
        try:
            self.chroma_collection.delete(where={"document_id": document_id})
        except Exception as e:
            logger.warning("Failed to delete Chroma vectors for %s: %s", document_id, str(e))


    # -------------------------------------------------------------
    # Retrieval
    # -------------------------------------------------------------
    def retrieve_relevant_chunks(
        self,
        document_id: str,
        query: str,
        top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Embeds the query and queries ChromaDB filtering strictly by document_id.
        """
        query_embedding = self.embedding_model.encode([query], convert_to_numpy=True).tolist()

        collection = self.chroma_collection
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=top_k,
            where={"document_id": document_id}
        )

        retrieved: List[Dict[str, Any]] = []
        if not results or not results.get("documents") or not results["documents"][0]:
            return retrieved

        docs = results["documents"][0]
        metadatas = results["metadatas"][0] if results.get("metadatas") else []
        distances = results["distances"][0] if results.get("distances") else []

        for i in range(len(docs)):
            meta = metadatas[i] if i < len(metadatas) else {}
            # Cosine distance to similarity (approx 1 - dist)
            relevance = round(1.0 - distances[i], 3) if i < len(distances) else None
            retrieved.append({
                "text": docs[i],
                "page": int(meta.get("page_number", 1)),
                "chunk_index": int(meta.get("chunk_index", i)),
                "relevance_score": relevance
            })

        return retrieved

    # -------------------------------------------------------------
    # PDF Doubt Solving
    # -------------------------------------------------------------
    def ask_document(self, document_id: str, question: str) -> Dict[str, Any]:
        """
        Grounded QA workflow:
        1. Validates document is ready.
        2. Retrieves relevant chunks strictly for this document.
        3. Prompts Groq LLM with context.
        4. Returns answer and source page snippets.
        """
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM documents WHERE id = ?", (document_id,))
            row = cursor.fetchone()
            if not row:
                raise DocumentNotFoundError(document_id)
            doc_record = dict(row)

        if doc_record["status"] != "ready":
            raise RAGException(
                f"Document is not ready for querying. Current status: '{doc_record['status']}'. "
                f"Reason: {doc_record.get('error_message') or 'Still processing'}",
                status_code=400
            )

        # Retrieve top 4 relevant chunks
        chunks = self.retrieve_relevant_chunks(document_id, question, top_k=4)

        if not chunks:
            return {
                "answer": "The uploaded PDF does not contain enough relevant information to answer this question.",
                "document_id": document_id,
                "document_name": doc_record["original_name"],
                "sources": []
            }

        # Build context string
        context_blocks = []
        for c in chunks:
            context_blocks.append(f"[Source Page {c['page']}]:\n{c['text']}")
        context_str = "\n\n".join(context_blocks)

        system_prompt = (
            "You are an expert Aptitude Practice Assistant answering a student's question based strictly on the provided PDF context.\n\n"
            "Grounding Rules:\n"
            "1. Answer the question using ONLY facts and methods directly supported by the context below.\n"
            "2. If the provided context does not contain enough relevant information to answer the question, clearly state: "
            "'The uploaded PDF does not contain enough relevant information to answer this question.'\n"
            "3. Do not extrapolate, hallucinate, or falsely claim that information comes from the document.\n"
            "4. Explain in clear, student-friendly language suitable for competitive campus placement preparation.\n"
            "5. Cite the relevant page numbers where applicable."
        )

        user_prompt = (
            f"Document Name: {doc_record['original_name']}\n\n"
            f"=== RETRIEVED CONTEXT FROM PDF ===\n{context_str}\n\n"
            f"=== STUDENT QUESTION ===\n{question}"
        )

        client = llm_service._get_client()
        try:
            response = client.chat.completions.create(
                model=settings.GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2,  # Low temperature for strict factual grounding
                max_tokens=1000,
            )
            answer = response.choices[0].message.content or ""
        except Exception as e:
            import groq
            if isinstance(e, groq.APIStatusError) and e.status_code == 404:
                logger.error("Groq model '%s' not found (HTTP 404) during document QA: %s", settings.GROQ_MODEL, str(e))
                raise LLMServiceException(
                    f"Configured Groq model '{settings.GROQ_MODEL}' was not found or is unavailable (HTTP 404). "
                    "Please verify that GROQ_MODEL in backend/.env is set to an active model (e.g. 'openai/gpt-oss-120b').",
                    status_code=502
                )
            logger.error("Groq generation failed for document ask: %s", str(e))
            raise LLMServiceException(f"AI service error during document QA: {str(e)}", status_code=502)

        sources = [{
            "page": c["page"],
            "chunk_index": c["chunk_index"],
            "text": c["text"],
            "relevance_score": c["relevance_score"]
        } for c in chunks]

        return {
            "answer": answer.strip(),
            "document_id": document_id,
            "document_name": doc_record["original_name"],
            "sources": sources
        }

    # -------------------------------------------------------------
    # PDF Question Generation
    # -------------------------------------------------------------
    def generate_questions(
        self,
        document_id: str,
        topic: Optional[str] = None,
        difficulty: str = "Medium",
        count: int = 5
    ) -> Dict[str, Any]:
        """
        Generates multiple-choice aptitude questions grounded in retrieved PDF content.
        Validates structure deterministically (4 options A-D, valid correct_option, explanation, sources).
        """
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM documents WHERE id = ?", (document_id,))
            row = cursor.fetchone()
            if not row:
                raise DocumentNotFoundError(document_id)
            doc_record = dict(row)

        if doc_record["status"] != "ready":
            raise RAGException(f"Document is not ready. Current status: '{doc_record['status']}'.", status_code=400)

        # Retrieve relevant chunks for topic, or representative chunks across document
        search_query = topic if (topic and topic.strip()) else "aptitude concepts formulas quantitative problems logical reasoning questions"
        chunks = self.retrieve_relevant_chunks(document_id, search_query, top_k=6)

        if not chunks:
            raise RAGException("Could not retrieve relevant content from this PDF to generate questions.", status_code=400)

        context_blocks = []
        for c in chunks:
            context_blocks.append(f"[Page {c['page']}]:\n{c['text']}")
        context_str = "\n\n".join(context_blocks)

        system_prompt = (
            "You are an expert Aptitude Test Question Designer for campus placement exams.\n"
            "Generate multiple-choice practice questions grounded strictly in the provided document context.\n\n"
            "Return ONLY a valid JSON array of objects with NO surrounding markdown backticks or commentary.\n"
            "JSON Object Schema:\n"
            "[\n"
            "  {\n"
            "    \"question\": \"Question statement...\",\n"
            "    \"options\": [\n"
            "      {\"id\": \"A\", \"text\": \"Option text\"},\n"
            "      {\"id\": \"B\", \"text\": \"Option text\"},\n"
            "      {\"id\": \"C\", \"text\": \"Option text\"},\n"
            "      {\"id\": \"D\", \"text\": \"Option text\"}\n"
            "    ],\n"
            "    \"correct_option\": \"A\",\n"
            "    \"explanation\": \"Step-by-step mathematical or logical solution\",\n"
            "    \"source_pages\": [1]\n"
            "  }\n"
            "]\n\n"
            "Strict Quality Rules:\n"
            "1. Generate exactly the requested number of questions.\n"
            "2. Options must have distinct values with unique IDs 'A', 'B', 'C', 'D'.\n"
            "3. 'correct_option' must be exactly one of 'A', 'B', 'C', or 'D'.\n"
            "4. 'source_pages' must contain only valid page numbers present in the provided context.\n"
            "5. The question must test aptitude, quantitative calculation, logical deductions, or concepts found in the context."
        )

        user_prompt = (
            f"Document: {doc_record['original_name']}\n"
            f"Topic Focus: {topic or 'Aptitude Concepts from Document'}\n"
            f"Difficulty: {difficulty}\n"
            f"Question Count: {count}\n\n"
            f"=== DOCUMENT CONTEXT ===\n{context_str}"
        )

        client = llm_service._get_client()
        try:
            response = client.chat.completions.create(
                model=settings.GROQ_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,
                max_tokens=2500,
            )
            raw_content = response.choices[0].message.content or ""
        except Exception as e:
            import groq
            if isinstance(e, groq.APIStatusError) and e.status_code == 404:
                logger.error("Groq model '%s' not found (HTTP 404) during question generation: %s", settings.GROQ_MODEL, str(e))
                raise LLMServiceException(
                    f"Configured Groq model '{settings.GROQ_MODEL}' was not found or is unavailable (HTTP 404). "
                    "Please verify that GROQ_MODEL in backend/.env is set to an active model (e.g. 'openai/gpt-oss-120b').",
                    status_code=502
                )
            logger.error("Groq question generation failed: %s", str(e))
            raise LLMServiceException(f"AI service error during question generation: {str(e)}", status_code=502)

        # Parse JSON
        import json
        clean_json_str = raw_content.strip()
        if clean_json_str.startswith("```json"):
            clean_json_str = clean_json_str[7:]
        elif clean_json_str.startswith("```"):
            clean_json_str = clean_json_str[3:]
        if clean_json_str.endswith("```"):
            clean_json_str = clean_json_str[:-3]
        clean_json_str = clean_json_str.strip()

        try:
            parsed_questions = json.loads(clean_json_str)
            if not isinstance(parsed_questions, list):
                raise ValueError("Generated JSON is not a list")
        except Exception as e:
            logger.error("Failed to parse generated questions JSON: %s. Raw: %s", str(e), raw_content[:500])
            raise RAGException("Failed to parse AI question generator output into structured format.", status_code=500)

        # Deterministic verification and structuring
        validated_questions = []
        available_pages = {c["page"] for c in chunks}

        for idx, q_data in enumerate(parsed_questions[:count]):
            q_text = str(q_data.get("question", "")).strip()
            raw_options = q_data.get("options", [])
            correct_opt = str(q_data.get("correct_option", "")).strip().upper()
            explanation = str(q_data.get("explanation", "")).strip()
            raw_sources = q_data.get("source_pages", [])

            # Validation checks
            if not q_text or len(raw_options) != 4 or correct_opt not in ["A", "B", "C", "D"]:
                continue

            formatted_options = []
            option_texts = set()
            is_valid_options = True
            for opt in raw_options:
                opt_id = str(opt.get("id", "")).strip().upper()
                opt_txt = str(opt.get("text", "")).strip()
                if opt_id not in ["A", "B", "C", "D"] or not opt_txt or opt_txt in option_texts:
                    is_valid_options = False
                    break
                option_texts.add(opt_txt)
                formatted_options.append({"id": opt_id, "text": opt_txt})

            if not is_valid_options:
                continue

            # Check source pages against available document pages
            valid_sources = []
            if isinstance(raw_sources, list):
                for p in raw_sources:
                    try:
                        p_int = int(p)
                        if p_int in available_pages or (1 <= p_int <= doc_record["page_count"]):
                            valid_sources.append(p_int)
                    except (ValueError, TypeError):
                        pass
            if not valid_sources:
                valid_sources = [chunks[0]["page"]]

            # Deterministic check: verify that correct_option matches one of the provided options
            matching_option = next((opt for opt in formatted_options if opt["id"] == correct_opt), None)
            is_verified = (matching_option is not None and len(explanation) > 10)

            validated_questions.append({
                "id": f"gen_{document_id[:8]}_{idx+1}_{uuid.uuid4().hex[:4]}",
                "question": q_text,
                "options": formatted_options,
                "correct_option": correct_opt,
                "explanation": explanation or "Derived from the uploaded study material.",
                "source_pages": sorted(list(set(valid_sources))),
                "is_grounded": True,
                "verified": is_verified
            })

        if not validated_questions:
            raise RAGException("Failed to generate structurally verified questions from the document content.", status_code=500)

        return {
            "document_id": document_id,
            "document_name": doc_record["original_name"],
            "topic": topic,
            "difficulty": difficulty,
            "questions": validated_questions
        }


# Global singleton instance
rag_service = RAGService()
