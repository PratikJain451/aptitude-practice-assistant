from fastapi import APIRouter, HTTPException
from app.schemas.api_models import DoubtRequest, DoubtResponse
from app.services.llm_service import llm_service, LLMServiceException

router = APIRouter(prefix="/ai", tags=["AI Doubt Solver"])

@router.post("/doubt", response_model=DoubtResponse)
def solve_doubt(request: DoubtRequest):
    """
    Direct LLM-based doubt resolution for aptitude, quantitative, logical, and verbal questions.
    Uses the configured Groq LLM model with pedagogical system instructions.
    """
    try:
        # Convert Pydantic conversation history objects to simple dicts
        history = (
            [{"role": msg.role, "content": msg.content} for msg in request.conversation_history]
            if request.conversation_history
            else None
        )

        result = llm_service.solve_doubt(
            question=request.question,
            topic=request.topic,
            conversation_history=history,
        )

        return DoubtResponse(
            answer=result["answer"],
            topic=result.get("topic"),
            model=result["model"],
        )
    except LLMServiceException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while processing your doubt with the AI engine."
        )
