import sqlite3
import os
from contextlib import contextmanager

DB_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "aptitude_assistant.db"))

def get_db_connection():
    """Returns a direct sqlite3 connection with Row factory enabled."""
    conn = sqlite3.connect(DB_FILE_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

@contextmanager
def get_db():
    conn = get_db_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    """Initializes the database schema if tables do not exist or migrates schema."""
    with get_db() as conn:
        cursor = conn.cursor()

        # Check existing columns in practice_attempts if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='practice_attempts'")
        table_exists = cursor.fetchone() is not None

        if table_exists:
            cursor.execute("PRAGMA table_info(practice_attempts)")
            columns = [row["name"] for row in cursor.fetchall()]
            if "question_id" not in columns or "selected_answer" not in columns:
                cursor.execute("DROP TABLE practice_attempts")
                table_exists = False

        if not table_exists:
            cursor.execute("""
                CREATE TABLE practice_attempts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question_id TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    difficulty TEXT NOT NULL,
                    selected_answer TEXT NOT NULL,
                    is_correct BOOLEAN NOT NULL,
                    time_spent_seconds INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

        # Mock test attempts session table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mock_test_sessions (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                topic TEXT NOT NULL,
                total_questions INTEGER NOT NULL,
                correct_answers INTEGER NOT NULL,
                time_spent_seconds INTEGER NOT NULL,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Uploaded PDF documents table for RAG
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id TEXT PRIMARY KEY,
                filename TEXT NOT NULL,
                original_name TEXT NOT NULL,
                file_size INTEGER NOT NULL,
                page_count INTEGER DEFAULT 0,
                chunk_count INTEGER DEFAULT 0,
                status TEXT NOT NULL,
                error_message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
