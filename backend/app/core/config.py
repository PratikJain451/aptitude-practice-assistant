from typing import List, Optional
import json
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Aptitude Practice Assistant API"
    ENVIRONMENT: str = "development"
    PORT: int = 8000
    HOST: str = "127.0.0.1"
    CORS_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173,http://localhost:3000"
    DATABASE_URL: str = "sqlite:///./aptitude_assistant.db"

    # LLM Settings (Groq)
    GROQ_API_KEY: Optional[str] = None
    GROQ_MODEL: str = "openai/gpt-oss-120b"
    GROQ_TIMEOUT_SECONDS: int = 30

    # RAG Settings
    DATA_DIR: str = "data"
    DOCUMENTS_DIR: str = "data/documents"
    CHROMA_PERSIST_DIR: str = "data/chroma_db"
    EMBEDDING_MODEL_NAME: str = "BAAI/bge-small-en-v1.5"
    MAX_FILE_SIZE_BYTES: int = 15 * 1024 * 1024  # 15 MB

    model_config = SettingsConfigDict(
        env_file=[
            ".env",
            "backend/.env",
            os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
        ],
        extra="ignore"
    )

    @property
    def cors_origins_list(self) -> List[str]:
        val = self.CORS_ORIGINS.strip()
        if val.startswith("[") and val.endswith("]"):
            try:
                return json.loads(val)
            except Exception:
                pass
        return [origin.strip() for origin in val.split(",") if origin.strip()]

settings = Settings()
