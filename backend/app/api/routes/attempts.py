from typing import List
from fastapi import APIRouter, HTTPException
from app.db.database import get_db
from app.schemas.api_models import CreateAttemptRequest, AttemptResponse

router = APIRouter(prefix="/attempts", tags=["Attempts"])

@router.post("", response_model=AttemptResponse, status_code=201)
def create_attempt(body: CreateAttemptRequest):
    """Saves a student's practice question attempt to the SQLite database."""
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO practice_attempts (
                    question_id, topic, difficulty, selected_answer, is_correct, time_spent_seconds
                ) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    body.question_id,
                    body.topic,
                    body.difficulty,
                    body.selected_answer,
                    1 if body.is_correct else 0,
                    body.time_spent_seconds or 0,
                ),
            )
            attempt_id = cursor.lastrowid

            cursor.execute(
                """
                SELECT id, question_id, topic, difficulty, selected_answer, is_correct, time_spent_seconds, created_at
                FROM practice_attempts
                WHERE id = ?
                """,
                (attempt_id,),
            )
            row = cursor.fetchone()
            if not row:
                raise HTTPException(status_code=500, detail="Failed to retrieve inserted attempt record.")

            return AttemptResponse(
                id=row["id"],
                question_id=row["question_id"],
                topic=row["topic"],
                difficulty=row["difficulty"],
                selected_answer=row["selected_answer"],
                is_correct=bool(row["is_correct"]),
                time_spent_seconds=row["time_spent_seconds"],
                created_at=str(row["created_at"]),
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error while saving attempt: {str(e)}")

@router.get("", response_model=List[AttemptResponse])
def get_attempts():
    """Returns the student's recorded attempts for the current local application."""
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, question_id, topic, difficulty, selected_answer, is_correct, time_spent_seconds, created_at
                FROM practice_attempts
                ORDER BY created_at DESC, id DESC
                LIMIT 100
                """
            )
            rows = cursor.fetchall()

            return [
                AttemptResponse(
                    id=row["id"],
                    question_id=row["question_id"],
                    topic=row["topic"],
                    difficulty=row["difficulty"],
                    selected_answer=row["selected_answer"],
                    is_correct=bool(row["is_correct"]),
                    time_spent_seconds=row["time_spent_seconds"],
                    created_at=str(row["created_at"]),
                )
                for row in rows
            ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error while fetching attempts: {str(e)}")

@router.delete("")
def delete_attempts():
    """Resets the student's recorded attempt history."""
    try:
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) as cnt FROM practice_attempts")
            count = cursor.fetchone()["cnt"]
            cursor.execute("DELETE FROM practice_attempts")
            return {
                "message": "Attempt history reset successfully",
                "deleted_count": count
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error while resetting attempts: {str(e)}")
