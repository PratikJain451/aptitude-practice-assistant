import logging
from typing import List, Optional, Dict, Any
from app.core.config import settings

logger = logging.getLogger(__name__)

class LLMServiceException(Exception):
    """Base exception for LLM service issues."""
    def __init__(self, message: str, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

class LLMConfigurationError(LLMServiceException):
    def __init__(self, message: str):
        super().__init__(message, status_code=503)

class LLMRateLimitError(LLMServiceException):
    def __init__(self, message: str):
        super().__init__(message, status_code=429)

class LLMAuthenticationError(LLMServiceException):
    def __init__(self, message: str):
        super().__init__(message, status_code=502)

class LLMTimeoutError(LLMServiceException):
    def __init__(self, message: str):
        super().__init__(message, status_code=504)

class LLMProviderError(LLMServiceException):
    def __init__(self, message: str):
        super().__init__(message, status_code=502)

SYSTEM_PROMPT = """You are an expert, encouraging Aptitude and Campus Placement Coach. Your purpose is to resolve college students' aptitude doubts, quantitative questions, logical reasoning puzzles, verbal ability problems, and placement exam strategies.

Core Guidelines:
1. Explain concepts in clear, beginner-friendly, educational language.
2. Formulas & Principles: State the formal standard mathematical or logical formula clearly.
3. Shortcuts vs Standard Methods: Explicitly distinguish between standard textbook derivations and competitive exam shortcuts/tricks.
4. Step-by-Step Calculation: Break down numerical calculations step-by-step with clean arithmetic.
5. Examples: Provide a mini-example where it aids understanding.
6. Ambiguity: If the student's question is incomplete or missing necessary numerical constraints, politely identify what information is missing and ask for clarification.
7. Mathematical Accuracy: Never hallucinate numbers or claim unverified assertions.
8. Focus: Keep explanations directly targeted on placement aptitude, quantitative ability, logical reasoning, and verbal comprehension. Keep formatting structured with clean markdown (bold, bullet points, numbered steps, math expressions)."""

class GroqLLMService:
    def __init__(self):
        pass

    @property
    def model(self) -> str:
        """Returns the currently configured Groq model name from settings."""
        return settings.GROQ_MODEL

    @property
    def timeout(self) -> int:
        return settings.GROQ_TIMEOUT_SECONDS

    def _get_client(self):
        api_key = settings.GROQ_API_KEY
        if not api_key or not api_key.strip():
            raise LLMConfigurationError(
                "GROQ_API_KEY is not configured in backend/.env. "
                "Please add your free Groq API key from https://console.groq.com/keys to backend/.env to enable live AI Doubt Solving."
            )
        import groq
        return groq.Groq(api_key=api_key.strip(), timeout=self.timeout)

    def solve_doubt(
        self,
        question: str,
        topic: Optional[str] = None,
        conversation_history: Optional[List[Dict[str, str]]] = None,
    ) -> Dict[str, Any]:
        """
        Generates structured aptitude explanations for student doubts using Groq LLM.
        """
        client = self._get_client()

        # Build message history with sensible guardrails
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # Append sanitized conversation history (max 10 recent messages)
        if conversation_history:
            recent_history = conversation_history[-10:]
            for item in recent_history:
                role = item.get("role")
                content = item.get("content")
                if role in ["user", "assistant"] and isinstance(content, str) and content.strip():
                    messages.append({
                        "role": role,
                        "content": content.strip()[:2000] # clamp message length
                    })

        # Append current user prompt
        user_content = f"[Topic: {topic}]\n{question}" if topic else question
        messages.append({"role": "user", "content": user_content})

        try:
            import groq
            response = client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3, # low temperature for reliable mathematical reasoning
                max_tokens=1500,
            )

            answer = response.choices[0].message.content
            if not answer or not answer.strip():
                raise LLMProviderError("Received empty response from the AI provider.")

            return {
                "answer": answer.strip(),
                "topic": topic,
                "model": self.model,
            }

        except groq.AuthenticationError as e:
            logger.error("Groq Authentication Error: Key invalid or rejected (credentials masked)")
            raise LLMAuthenticationError(
                "Groq authentication failed. Please verify that your GROQ_API_KEY in backend/.env is valid."
            )
        except groq.RateLimitError as e:
            logger.warning("Groq Rate Limit Error for model '%s': %s", self.model, str(e))
            raise LLMRateLimitError(
                "Groq API rate limit exceeded. Please wait a moment before asking another question."
            )
        except groq.APITimeoutError as e:
            logger.error("Groq Timeout Error for model '%s' after %ss: %s", self.model, self.timeout, str(e))
            raise LLMTimeoutError(
                "AI request timed out. The model took too long to generate a response. Please try again."
            )
        except groq.APIConnectionError as e:
            logger.error("Groq Connection Error: failed to connect to Groq endpoint: %s", str(e))
            raise LLMProviderError(
                "Failed to connect to Groq API. Please check network connectivity."
            )
        except groq.APIStatusError as e:
            logger.error("Groq API Status Error: status=%s, model='%s', detail=%s", e.status_code, self.model, str(e))
            if e.status_code == 404:
                raise LLMProviderError(
                    f"Configured Groq model '{self.model}' was not found or is no longer available on Groq (HTTP 404). "
                    "Please verify that GROQ_MODEL in backend/.env is set to an active Groq model (e.g. 'openai/gpt-oss-120b')."
                )
            raise LLMProviderError(
                f"Groq provider returned an error (status {e.status_code}). Please try again later."
            )
        except LLMServiceException:
            raise
        except Exception as e:
            logger.error("Unexpected LLM error: %s", str(e), exc_info=True)
            raise LLMProviderError(
                "An unexpected error occurred while communicating with the AI service."
            )

# Global service instance
llm_service = GroqLLMService()
