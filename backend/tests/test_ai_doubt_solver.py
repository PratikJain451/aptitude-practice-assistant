from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)

# 1. Request Validation Tests
def test_doubt_request_validation():
    # Empty question
    res = client.post("/api/ai/doubt", json={"question": ""})
    assert res.status_code == 422

    # Question too short (< 2 chars)
    res = client.post("/api/ai/doubt", json={"question": "a"})
    assert res.status_code == 422

    # Valid payload structure
    with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_choice = MagicMock()
        mock_choice.message.content = "Explanation of relative speed..."
        mock_client.chat.completions.create.return_value = MagicMock(choices=[mock_choice])
        mock_get_client.return_value = mock_client

        res = client.post(
            "/api/ai/doubt",
            json={
                "question": "What is the relative speed formula for two trains moving towards each other?",
                "topic": "Quantitative Aptitude",
                "conversation_history": [
                    {"role": "user", "content": "Hello coach"},
                    {"role": "assistant", "content": "Hello! How can I help you today?"}
                ]
            }
        )
        assert res.status_code == 200
        data = res.json()
        assert data["answer"] == "Explanation of relative speed..."
        assert data["topic"] == "Quantitative Aptitude"
        assert "model" in data

# 2. Missing Configuration Error Test
def test_doubt_missing_groq_api_key():
    # Force GROQ_API_KEY to None / empty
    with patch.object(settings, "GROQ_API_KEY", None):
        res = client.post("/api/ai/doubt", json={"question": "How to solve syllogisms?"})
        assert res.status_code == 503
        data = res.json()
        assert "GROQ_API_KEY is not configured" in data["detail"]

# 3. Successful Provider Response via Mock
def test_doubt_successful_provider_response():
    with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_choice = MagicMock()
        mock_choice.message.content = "To solve Time and Work using the LCM method:\n1. Total Work = LCM\n2. Efficiency = Work / Days"
        mock_client.chat.completions.create.return_value = MagicMock(choices=[mock_choice])
        mock_get_client.return_value = mock_client

        res = client.post(
            "/api/ai/doubt",
            json={
                "question": "Explain LCM method in Time and Work",
                "topic": "Time and Work"
            }
        )
        assert res.status_code == 200
        data = res.json()
        assert "LCM method" in data["answer"]
        assert data["topic"] == "Time and Work"
        assert data["model"] == settings.GROQ_MODEL

# 4. Provider Error Handling - Authentication Error
def test_doubt_authentication_error_handling():
    import groq
    with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
        mock_client = MagicMock()
        # Mock AuthenticationError
        mock_client.chat.completions.create.side_effect = groq.AuthenticationError(
            message="Invalid API Key",
            response=MagicMock(status_code=401),
            body={"error": {"message": "Invalid API Key"}}
        )
        mock_get_client.return_value = mock_client

        res = client.post("/api/ai/doubt", json={"question": "Explain permutations vs combinations"})
        assert res.status_code == 502
        assert "Groq authentication failed" in res.json()["detail"]

# 5. Provider Error Handling - Rate Limit Error
def test_doubt_rate_limit_error_handling():
    import groq
    with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = groq.RateLimitError(
            message="Rate limit reached",
            response=MagicMock(status_code=429),
            body={"error": {"message": "Rate limit reached"}}
        )
        mock_get_client.return_value = mock_client

        res = client.post("/api/ai/doubt", json={"question": "What is Bayes theorem?"})
        assert res.status_code == 429
        assert "rate limit exceeded" in res.json()["detail"].lower()

# 6. Provider Error Handling - Timeout Error
def test_doubt_timeout_error_handling():
    import groq
    with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = groq.APITimeoutError(
            request=MagicMock()
        )
        mock_get_client.return_value = mock_client

        res = client.post("/api/ai/doubt", json={"question": "Solve train distance problem"})
        assert res.status_code == 504
        assert "timed out" in res.json()["detail"].lower()

# 7. Provider Error Handling - Model Not Found (HTTP 404)
def test_doubt_model_not_found_404_error_handling():
    import groq
    with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = groq.APIStatusError(
            message="The model does not exist or you do not have access to it.",
            response=MagicMock(status_code=404),
            body={"error": {"message": "The model does not exist"}}
        )
        mock_get_client.return_value = mock_client

        res = client.post("/api/ai/doubt", json={"question": "Solve distance formula"})
        assert res.status_code == 502
        detail = res.json()["detail"]
        assert "404" in detail or "not found" in detail.lower()
        assert "GROQ_MODEL" in detail

# 8. Model Configuration & Credential Safety
def test_doubt_model_setting_and_credential_safety():
    from app.services.llm_service import llm_service
    # Verify dynamic property resolves to current settings
    assert llm_service.model == settings.GROQ_MODEL
    # Verify default model is openai/gpt-oss-120b
    assert "gpt-oss-120b" in settings.GROQ_MODEL

    # Verify that sensitive API keys are never exposed in error responses
    import groq
    fake_key = "gsk_super_secret_key_12345"
    with patch("app.services.llm_service.llm_service._get_client") as mock_get_client:
        mock_client = MagicMock()
        mock_client.chat.completions.create.side_effect = groq.AuthenticationError(
            message=f"Invalid Authorization header Bearer {fake_key}",
            response=MagicMock(status_code=401),
            body={"error": {"message": f"Invalid key {fake_key}"}}
        )
        mock_get_client.return_value = mock_client

        res = client.post("/api/ai/doubt", json={"question": "Explain probability of drawing aces"})
        assert res.status_code == 502
        response_text = str(res.json())
        assert fake_key not in response_text


