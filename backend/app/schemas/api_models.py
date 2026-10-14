from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class OptionModel(BaseModel):
    id: str
    text: str

class QuestionDisplayResponse(BaseModel):
    id: str
    topic: str
    difficulty: str
    question: str
    options: List[OptionModel]

class TopicCountResponse(BaseModel):
    topic: str
    question_count: int

class SubmitAnswerRequest(BaseModel):
    selected_answer: str = Field(..., min_length=1, max_length=10, description="Selected option ID, e.g. 'A', 'B', 'C', 'D'")

class SubmitAnswerResponse(BaseModel):
    question_id: str
    is_correct: bool
    correct_answer: str
    explanation: str
    formula: Optional[str] = None

class CreateAttemptRequest(BaseModel):
    question_id: str
    topic: str
    difficulty: str
    selected_answer: str
    is_correct: bool
    time_spent_seconds: Optional[int] = 0

class AttemptResponse(BaseModel):
    id: int
    question_id: str
    topic: str
    difficulty: str
    selected_answer: str
    is_correct: bool
    time_spent_seconds: int
    created_at: str

class TopicPerformanceMetric(BaseModel):
    topic: str
    attempted: int
    correct: int
    accuracy: float
    avg_time_seconds: float

class PerformanceSummaryResponse(BaseModel):
    questions_attempted: int
    correct_answers: int
    accuracy: float
    topic_wise_performance: List[TopicPerformanceMetric]
    recent_attempts: List[AttemptResponse]

# AI Doubt Solver Schemas
class ChatMessageItem(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(..., min_length=1, max_length=2000)

class DoubtRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=2000, description="The student's aptitude doubt or problem statement")
    topic: Optional[str] = Field(None, max_length=100, description="Optional aptitude topic")
    conversation_history: Optional[List[ChatMessageItem]] = Field(default=None, max_length=10, description="Optional previous conversation turns (up to 10)")

class DoubtResponse(BaseModel):
    answer: str
    topic: Optional[str] = None
    model: str

# PDF RAG Schemas
class DocumentResponse(BaseModel):
    id: str
    filename: str
    original_name: str
    file_size: int
    page_count: int
    chunk_count: int
    status: str
    error_message: Optional[str] = None
    created_at: str
    updated_at: str

class DocumentListResponse(BaseModel):
    documents: List[DocumentResponse]
    total: int

class DocumentAskRequest(BaseModel):
    question: str = Field(..., min_length=2, max_length=2000, description="The student's question based on the PDF content")

class SourceSnippet(BaseModel):
    page: int
    chunk_index: int
    text: str
    relevance_score: Optional[float] = None

class DocumentAskResponse(BaseModel):
    answer: str
    document_id: str
    document_name: str
    sources: List[SourceSnippet]

class GenerateQuestionsRequest(BaseModel):
    topic: Optional[str] = Field(None, max_length=100, description="Optional focus topic within the document")
    difficulty: Literal["Easy", "Medium", "Hard"] = Field("Medium", description="Question difficulty level")
    count: int = Field(default=5, ge=1, le=10, description="Number of questions to generate (1 to 10)")

class GeneratedQuestionItem(BaseModel):
    id: str
    question: str
    options: List[OptionModel]
    correct_option: str
    explanation: str
    source_pages: List[int]
    is_grounded: bool = True
    verified: bool = False

class GenerateQuestionsResponse(BaseModel):
    document_id: str
    document_name: str
    topic: Optional[str] = None
    difficulty: str
    questions: List[GeneratedQuestionItem]
