# Aptitude Practice Assistant

A production-quality, focused web application engineered for college students preparing for campus placement aptitude examinations (TCS, Infosys, Wipro, Accenture, Cognizant, etc.).

---

## 1. Architecture & Tech Stack

The project separates frontend and backend into isolated environments:

### Frontend
- **React 19** with **TypeScript**
- **Vite 8** for fast bundling and hot module replacement
- **Tailwind CSS v4** (`@tailwindcss/vite`) for restrained, typography-first UI
- **Lucide React** for consistent vector iconography
- **React Router v7** for single-page client routing
- **Inter** typography from Google Fonts

### Backend
- **Python 3.11+**
- **FastAPI** for high-performance async REST APIs
- **Groq LLM SDK** with `llama-3.3-70b-versatile` for fast, pedagogical step-by-step doubt resolution
- **Pydantic & Pydantic-Settings** for strict schema validation and environment management
- **Uvicorn** ASGI server
- **SQLite** database (`aptitude_assistant.db`) for parameterized local persistence of attempts, topics, and mock sessions
- **Pytest** for comprehensive integration test suites

---

## 2. Project Directory Structure

```text
aptitude-practice-assistant/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       ├── health.py          # GET /api/health
│   │   │       ├── questions.py       # GET /api/questions/topics, GET /api/questions, POST /api/questions/{id}/submit
│   │   │       ├── attempts.py        # POST /api/attempts, GET /api/attempts, DELETE /api/attempts
│   │   │       ├── performance.py     # GET /api/performance/summary
│   │   │       └── ai.py              # POST /api/ai/doubt
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py              # Pydantic v2 Settings & CORS configuration
│   │   ├── data/
│   │   │   ├── __init__.py
│   │   │   └── questions.py           # Curated question bank (60 verified questions across 10 topics)
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   └── database.py            # SQLite schema initialization & connections
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── api_models.py          # Pydantic request and response models
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── llm_service.py         # Isolated Groq LLM service with prompt engineering
│   │   ├── __init__.py
│   │   └── main.py                    # FastAPI application entrypoint with lifespan events
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_practice_engine.py    # 8 Practice engine verification test cases
│   │   └── test_ai_doubt_solver.py    # 6 AI Doubt Solver verification test cases
│   ├── .env.example                   # Environment variable template
│   └── requirements.txt               # Python package dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/                # Badge, Button, Card, EmptyState
│   │   │   └── layout/                # Sidebar, TopBar, AppLayout
│   │   ├── data/                      # Local topic definitions & fallback samples
│   │   ├── pages/                     # Overview, Practice, MockTests, DoubtSolver, PdfStudy, Performance
│   │   ├── services/                  # api.ts (backend client) & storage.ts (client persistence)
│   │   ├── types/                     # TypeScript data interfaces and API models
│   │   ├── App.tsx                    # Route definitions
│   │   ├── index.css                  # Tailwind v4 import & Inter styling
│   │   └── main.tsx
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── .gitignore
└── README.md
```

---

## 3. Getting Started on Windows (PowerShell)

### Prerequisites
- **Node.js** (v18 or higher recommended)
- **Python** (v3.10 or higher)

---

### Step 3.1: Running the Backend (FastAPI)

1. Open PowerShell and navigate to the `backend` directory:
   ```powershell
   cd c:\Users\Lenovo\OneDrive\Desktop\aptitude-practice-assistant\backend
   ```

2. (Optional but recommended) Create and activate a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

4. Configure your environment:
   ```powershell
   Copy-Item .env.example .env
   ```
   Open `backend/.env` and insert your free Groq API key:
   ```env
   GROQ_API_KEY=gsk_your_actual_key_here
   GROQ_MODEL=llama-3.3-70b-versatile
   GROQ_TIMEOUT_SECONDS=30
   ```
   *(Obtain a free key at [https://console.groq.com/keys](https://console.groq.com/keys)).*

5. Run the FastAPI development server:
   ```powershell
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

6. Verify the backend:
   - **Health Endpoint**: `http://127.0.0.1:8000/api/health`
   - **Interactive API Documentation (Swagger UI)**: `http://127.0.0.1:8000/docs`

---

### Step 3.2: Running the Frontend (React + Vite)

1. Open a new PowerShell terminal and navigate to the `frontend` directory:
   ```powershell
   cd c:\Users\Lenovo\OneDrive\Desktop\aptitude-practice-assistant\frontend
   ```

2. Install npm packages (if not already installed):
   ```powershell
   npm install
   ```

3. Start the Vite local development server:
   ```powershell
   npm run dev
   ```

4. Open `http://localhost:5173` in your browser.

---

## 4. API Endpoints Reference

### AI Doubt Solver
- `POST /api/ai/doubt`:
  - **Request Body**:
    ```json
    {
      "question": "How do I solve 'A can do a work in 10 days and B in 15 days'?",
      "topic": "Time and Work",
      "conversation_history": [
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
      ]
    }
    ```
  - **Response Body**:
    ```json
    {
      "answer": "To solve this problem using the LCM unitary method: ...",
      "topic": "Time and Work",
      "model": "llama-3.3-70b-versatile"
    }
    ```
  - **Status Codes**: `200 OK`, `422 Unprocessable Entity` (validation), `503 Service Unavailable` (missing `GROQ_API_KEY` configuration), `429 Too Many Requests` (rate limit).

### PDF Document RAG Pipeline
- `POST /api/documents/upload`:
  - Accepts multipart PDF file upload (strictly `.pdf`, magic header `b"%PDF-"`, max 15 MB).
  - Extracts text page-by-page via PyMuPDF (`fitz`).
  - Detects empty/scanned PDFs lacking extractable text and returns `422 Unprocessable Content`.
  - Splits text into chunks (~500–700 characters, ~90 character overlap) and preserves document ID, document name, page number, and chunk index.
  - Embeds passages using `BAAI/bge-small-en-v1.5` and stores them in persistent ChromaDB (`backend/data/chroma_db`).
- `GET /api/documents`: Lists all uploaded documents, page counts, chunk counts, and processing statuses (`ready`, `processing`, `failed`, `uploaded`).
- `GET /api/documents/{document_id}`: Retrieves single document metadata.
- `DELETE /api/documents/{document_id}`: Atomically deletes the document record from SQLite, removes physical file from disk, and purges all associated vector embeddings from ChromaDB.
- `POST /api/documents/{document_id}/ask`: Grounded PDF doubt solver. Retrieves top chunks with Chroma document isolation filter, feeds retrieved context into Groq LLM, and returns answers with source page citations. Explicitly states if the PDF lacks sufficient context.
- `POST /api/documents/{document_id}/generate-questions`: Generates structured multiple-choice questions grounded strictly in the PDF content with deterministic schema validation.

### Questions & Topics
- `GET /api/questions/topics`: Lists available syllabus topics with question counts.
- `GET /api/questions`: Fetches sanitized questions with optional `topic`, `difficulty`, and `limit` query parameters. Hides correct answers and explanations until submission.
- `POST /api/questions/{question_id}/submit`: Evaluates user answer on the backend and returns correctness, correct option, explanation, and formula.

### Attempts & Performance Tracking
- `POST /api/attempts`: Records an answered question attempt to the SQLite database.
- `GET /api/attempts`: Lists the student's recorded attempts.
- `GET /api/performance/summary`: Returns real calculated metrics (attempted, correct, accuracy %, topic breakdown, recent attempts).
- `DELETE /api/attempts`: Resets stored attempt history.

---

## 5. RAG Pipeline Requirements & Model Memory Footprint

### Embedding Model Details
- **Model**: `BAAI/bge-small-en-v1.5` (via `sentence-transformers==6.1.0`)
- **Download Size**: ~133 MB (automatically cached in `~/.cache/huggingface/hub` on first invocation)
- **Runtime Memory Footprint**: ~250–350 MB RAM
- **Hardware Requirements**: Runs fast and reliably on standard multi-core consumer CPUs without requiring a dedicated GPU or CUDA setup.

### Persistent Vector Storage
- **ChromaDB**: Stored locally in `backend/data/chroma_db` using `chromadb.PersistentClient` with cosine similarity (`hnsw:space: "cosine"`).
- **Physical Documents**: Stored in `backend/data/documents` outside public frontend assets.

> [!NOTE]
> **Single-User Architecture**: This initial application version is designed as a single-user local study tool. User authentication, access tokens, and multi-tenant isolation are intentionally not implemented in this milestone.

---

## 6. Automated Testing & Verification Commands

- **Run All Backend Tests (24/24 Passing)**:
  ```powershell
  cd c:\Users\Lenovo\OneDrive\Desktop\aptitude-practice-assistant\backend
  python -m pytest tests/
  ```

- **Run Frontend Production Build**:
  ```powershell
  cd c:\Users\Lenovo\OneDrive\Desktop\aptitude-practice-assistant\frontend
  npm run build
  ```
