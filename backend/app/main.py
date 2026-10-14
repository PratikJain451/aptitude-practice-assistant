from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes import health, questions, attempts, performance, ai, documents
from app.db.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize SQLite schema on startup
    init_db()
    yield

app = FastAPI(
    title=settings.APP_NAME,
    description="Backend API service for Aptitude Practice Assistant",
    version="0.3.0",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(questions.router, prefix="/api", tags=["Questions"])
app.include_router(attempts.router, prefix="/api", tags=["Attempts"])
app.include_router(performance.router, prefix="/api", tags=["Performance"])
app.include_router(ai.router, prefix="/api", tags=["AI Doubt Solver"])
app.include_router(documents.router, prefix="/api", tags=["PDF Documents & RAG"])

@app.get("/")
def root():
    return {
        "message": "Aptitude Practice Assistant API is running.",
        "docs_url": "/docs",
        "health_check": "/api/health",
        "topics_url": "/api/questions/topics",
        "questions_url": "/api/questions",
        "performance_url": "/api/performance/summary",
        "ai_doubt_url": "/api/ai/doubt"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=True)
