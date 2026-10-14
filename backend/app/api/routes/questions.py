from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query, Path
from app.data.questions import QUESTIONS_DATA, QUESTIONS_BY_ID, TOPICS_LIST
from app.schemas.api_models import (
    TopicCountResponse,
    QuestionDisplayResponse,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
    OptionModel,
)

router = APIRouter(prefix="/questions", tags=["Questions"])

@router.get("/topics", response_model=List[TopicCountResponse])
def get_topics():
    """Returns available topics and their question counts in the curated question bank."""
    counts = {topic: 0 for topic in TOPICS_LIST}
    for q in QUESTIONS_DATA:
        topic = q.get("topic")
        if topic in counts:
            counts[topic] += 1
        else:
            counts[topic] = 1

    return [
        TopicCountResponse(topic=topic, question_count=counts[topic])
        for topic in TOPICS_LIST
    ]

@router.get("", response_model=List[QuestionDisplayResponse])
def get_questions(
    topic: Optional[str] = Query(None, description="Filter by topic name"),
    difficulty: Optional[str] = Query(None, description="Filter by difficulty: Easy, Medium, or Hard"),
    limit: Optional[int] = Query(None, ge=1, le=50, description="Number of questions to return"),
):
    """
    Returns sanitized questions without revealing correct answers or explanations.
    Validates parameters and returns clear error if available questions are insufficient.
    """
    filtered = list(QUESTIONS_DATA)

    # 1. Validate and filter topic if provided
    if topic:
        # Case-insensitive match against registered topics
        matched_topic = next((t for t in TOPICS_LIST if t.lower() == topic.strip().lower()), None)
        if not matched_topic:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid topic '{topic}'. Must be one of: {', '.join(TOPICS_LIST)}"
            )
        filtered = [q for q in filtered if q["topic"] == matched_topic]

    # 2. Validate and filter difficulty if provided
    if difficulty:
        valid_difficulties = ["Easy", "Medium", "Hard"]
        matched_diff = next((d for d in valid_difficulties if d.lower() == difficulty.strip().lower()), None)
        if not matched_diff:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid difficulty '{difficulty}'. Must be one of: {', '.join(valid_difficulties)}"
            )
        filtered = [q for q in filtered if q["difficulty"] == matched_diff]

    # 3. Validate sufficient question count if limit requested
    if limit is not None:
        if len(filtered) < limit:
            raise HTTPException(
                status_code=400,
                detail=(
                    f"Insufficient questions for the selected criteria. "
                    f"Requested {limit}, but only {len(filtered)} available."
                )
            )
        filtered = filtered[:limit]

    # 4. Map to display response strictly hiding correct_answer and explanation
    return [
        QuestionDisplayResponse(
            id=q["id"],
            topic=q["topic"],
            difficulty=q["difficulty"],
            question=q["question"],
            options=[OptionModel(id=opt["id"], text=opt["text"]) for opt in q["options"]],
        )
        for q in filtered
    ]

@router.post("/{question_id}/submit", response_model=SubmitAnswerResponse)
def submit_question_answer(
    question_id: str = Path(..., description="The unique question ID"),
    body: SubmitAnswerRequest = ...,
):
    """
    Evaluates the student's selected answer on the backend.
    Returns correctness, correct option, explanation, and formula.
    """
    question = QUESTIONS_BY_ID.get(question_id)
    if not question:
        raise HTTPException(
            status_code=404,
            detail=f"Question with ID '{question_id}' not found."
        )

    user_choice = body.selected_answer.strip().upper()
    correct_choice = question["correct_answer"].strip().upper()
    is_correct = (user_choice == correct_choice)

    return SubmitAnswerResponse(
        question_id=question["id"],
        is_correct=is_correct,
        correct_answer=correct_choice,
        explanation=question["explanation"],
        formula=question.get("formula"),
    )
