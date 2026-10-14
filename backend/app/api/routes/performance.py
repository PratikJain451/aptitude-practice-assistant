from typing import List
from fastapi import APIRouter, HTTPException
from app.db.database import get_db
from app.schemas.api_models import (
    PerformanceSummaryResponse,
    TopicPerformanceMetric,
    AttemptResponse,
)

router = APIRouter(prefix="/performance", tags=["Performance"])

@router.get("/summary", response_model=PerformanceSummaryResponse)
def get_performance_summary():
    """
    Returns real metrics calculated strictly from stored attempts:
    - Questions attempted
    - Correct answers
    - Accuracy percentage
    - Topic-wise performance breakdown
    - Recent attempts
    """
    try:
        with get_db() as conn:
            cursor = conn.cursor()

            # 1. Total counts
            cursor.execute(
                """
                SELECT
                    COUNT(*) as total_attempted,
                    SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) as total_correct
                FROM practice_attempts
                """
            )
            overall = cursor.fetchone()
            total_attempted = overall["total_attempted"] or 0
            total_correct = overall["total_correct"] or 0
            overall_accuracy = (
                round((total_correct / total_attempted) * 100, 1)
                if total_attempted > 0
                else 0.0
            )

            # 2. Topic-wise aggregation
            cursor.execute(
                """
                SELECT
                    topic,
                    COUNT(*) as attempted,
                    SUM(CASE WHEN is_correct = 1 THEN 1 ELSE 0 END) as correct,
                    AVG(time_spent_seconds) as avg_time
                FROM practice_attempts
                GROUP BY topic
                ORDER BY attempted DESC, topic ASC
                """
            )
            topic_rows = cursor.fetchall()
            topic_performance: List[TopicPerformanceMetric] = []
            for tr in topic_rows:
                att = tr["attempted"] or 0
                corr = tr["correct"] or 0
                acc = round((corr / att) * 100, 1) if att > 0 else 0.0
                avg_time = round(tr["avg_time"] or 0.0, 1)
                topic_performance.append(
                    TopicPerformanceMetric(
                        topic=tr["topic"],
                        attempted=att,
                        correct=corr,
                        accuracy=acc,
                        avg_time_seconds=avg_time,
                    )
                )

            # 3. Recent attempts (last 10)
            cursor.execute(
                """
                SELECT id, question_id, topic, difficulty, selected_answer, is_correct, time_spent_seconds, created_at
                FROM practice_attempts
                ORDER BY created_at DESC, id DESC
                LIMIT 10
                """
            )
            recent_rows = cursor.fetchall()
            recent_attempts = [
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
                for row in recent_rows
            ]

            return PerformanceSummaryResponse(
                questions_attempted=total_attempted,
                correct_answers=total_correct,
                accuracy=overall_accuracy,
                topic_wise_performance=topic_performance,
                recent_attempts=recent_attempts,
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error while generating performance summary: {str(e)}"
        )
