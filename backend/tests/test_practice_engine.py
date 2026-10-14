import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import init_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    init_db()
    # Reset attempts table before each test
    client.delete("/api/attempts")
    yield
    client.delete("/api/attempts")

# 1. Listing topics
def test_1_listing_topics():
    response = client.get("/api/questions/topics")
    assert response.status_code == 200
    topics = response.json()
    assert len(topics) >= 10
    topic_names = [t["topic"] for t in topics]
    assert "Quantitative Aptitude" in topic_names
    assert "Logical Reasoning" in topic_names
    assert "Time and Work" in topic_names
    assert "Percentages" in topic_names
    for t in topics:
        assert t["question_count"] >= 5

# 2. Filtering questions by topic and difficulty
def test_2_filtering_questions():
    response = client.get("/api/questions?topic=Time and Work&difficulty=Easy&limit=2")
    assert response.status_code == 200
    questions = response.json()
    assert len(questions) == 2
    for q in questions:
        assert q["topic"] == "Time and Work"
        assert q["difficulty"] == "Easy"
        assert len(q["options"]) == 4

    # Test error on insufficient questions
    insufficient_response = client.get("/api/questions?topic=Time and Work&difficulty=Easy&limit=50")
    assert insufficient_response.status_code == 400
    assert "Insufficient questions" in insufficient_response.json()["detail"]

# 3. Ensuring correct answers are NOT returned before submission
def test_3_no_answers_before_submission():
    response = client.get("/api/questions?limit=5")
    assert response.status_code == 200
    questions = response.json()
    assert len(questions) == 5
    for q in questions:
        assert "correct_answer" not in q
        assert "explanation" not in q
        assert "formula" not in q
        assert "id" in q
        assert "question" in q
        assert "options" in q

# 4. Correct answer evaluation
def test_4_correct_answer_evaluation():
    # Question tw-1 has correct_answer = 'B'
    payload = {"selected_answer": "B"}
    response = client.post("/api/questions/tw-1/submit", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["question_id"] == "tw-1"
    assert data["is_correct"] is True
    assert data["correct_answer"] == "B"
    assert "explanation" in data and len(data["explanation"]) > 0
    assert "formula" in data

# 5. Incorrect answer evaluation
def test_5_incorrect_answer_evaluation():
    # Question tw-1 correct answer is 'B', submit 'A'
    payload = {"selected_answer": "A"}
    response = client.post("/api/questions/tw-1/submit", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["question_id"] == "tw-1"
    assert data["is_correct"] is False
    assert data["correct_answer"] == "B"
    assert "explanation" in data

# 6. Saving attempts
def test_6_saving_attempts():
    attempt_payload = {
        "question_id": "tw-1",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "selected_answer": "B",
        "is_correct": True,
        "time_spent_seconds": 25
    }
    create_res = client.post("/api/attempts", json=attempt_payload)
    assert create_res.status_code == 201
    created_data = create_res.json()
    assert created_data["question_id"] == "tw-1"
    assert created_data["is_correct"] is True
    assert created_data["time_spent_seconds"] == 25

    # Verify retrieval
    get_res = client.get("/api/attempts")
    assert get_res.status_code == 200
    attempts_list = get_res.json()
    assert len(attempts_list) == 1
    assert attempts_list[0]["question_id"] == "tw-1"

# 7. Performance calculations
def test_7_performance_calculations():
    # Insert 3 attempts: 2 correct, 1 incorrect
    client.post("/api/attempts", json={
        "question_id": "tw-1",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "selected_answer": "B",
        "is_correct": True,
        "time_spent_seconds": 20
    })
    client.post("/api/attempts", json={
        "question_id": "tw-2",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "selected_answer": "C",
        "is_correct": True,
        "time_spent_seconds": 40
    })
    client.post("/api/attempts", json={
        "question_id": "pct-1",
        "topic": "Percentages",
        "difficulty": "Easy",
        "selected_answer": "A",
        "is_correct": False,
        "time_spent_seconds": 30
    })

    summary_res = client.get("/api/performance/summary")
    assert summary_res.status_code == 200
    summary = summary_res.json()
    assert summary["questions_attempted"] == 3
    assert summary["correct_answers"] == 2
    assert summary["accuracy"] == 66.7
    assert len(summary["recent_attempts"]) == 3

    # Check topic wise breakdown
    tw_perf = next((t for t in summary["topic_wise_performance"] if t["topic"] == "Time and Work"), None)
    assert tw_perf is not None
    assert tw_perf["attempted"] == 2
    assert tw_perf["correct"] == 2
    assert tw_perf["accuracy"] == 100.0
    assert tw_perf["avg_time_seconds"] == 30.0

    pct_perf = next((t for t in summary["topic_wise_performance"] if t["topic"] == "Percentages"), None)
    assert pct_perf is not None
    assert pct_perf["attempted"] == 1
    assert pct_perf["correct"] == 0
    assert pct_perf["accuracy"] == 0.0

# 8. Resetting attempt history
def test_8_resetting_attempt_history():
    # Insert 1 attempt
    client.post("/api/attempts", json={
        "question_id": "tw-1",
        "topic": "Time and Work",
        "difficulty": "Easy",
        "selected_answer": "B",
        "is_correct": True,
        "time_spent_seconds": 15
    })

    # Verify attempt exists
    assert len(client.get("/api/attempts").json()) == 1

    # Delete attempts
    del_res = client.delete("/api/attempts")
    assert del_res.status_code == 200
    assert del_res.json()["deleted_count"] == 1

    # Verify attempts are cleared
    assert len(client.get("/api/attempts").json()) == 0

    # Verify performance summary reflects empty state
    summary_res = client.get("/api/performance/summary")
    summary = summary_res.json()
    assert summary["questions_attempted"] == 0
    assert summary["correct_answers"] == 0
    assert summary["accuracy"] == 0.0
    assert len(summary["topic_wise_performance"]) == 0

# 9. Coding-Decoding 10-Question Availability Test
def test_9_coding_decoding_10_questions_availability():
    response = client.get("/api/questions?topic=Coding-Decoding&limit=10")
    assert response.status_code == 200
    questions = response.json()
    assert len(questions) == 10
    # Verify all returned questions are unique
    unique_ids = set(q["id"] for q in questions)
    assert len(unique_ids) == 10
    for q in questions:
        assert q["topic"] == "Coding-Decoding"
        assert len(q["options"]) == 4

# 10. Coding-Decoding Structure and Evaluation Test
def test_10_coding_decoding_structure_and_evaluation():
    # Submit correct answer for cd-1 ('A')
    res_correct = client.post("/api/questions/cd-1/submit", json={"selected_answer": "A"})
    assert res_correct.status_code == 200
    assert res_correct.json()["is_correct"] is True
    assert res_correct.json()["correct_answer"] == "A"

    # Submit incorrect answer for cd-1 ('B')
    res_incorrect = client.post("/api/questions/cd-1/submit", json={"selected_answer": "B"})
    assert res_incorrect.status_code == 200
    assert res_incorrect.json()["is_correct"] is False
    assert res_incorrect.json()["correct_answer"] == "A"

    # Verify cd-5 evaluation (PHYSI is C)
    res_cd5 = client.post("/api/questions/cd-5/submit", json={"selected_answer": "C"})
    assert res_cd5.status_code == 200
    assert res_cd5.json()["is_correct"] is True
    assert res_cd5.json()["correct_answer"] == "C"

    # Verify newly added question cd-9 (MATH sum is 42, option C)
    res_cd9 = client.post("/api/questions/cd-9/submit", json={"selected_answer": "C"})
    assert res_cd9.status_code == 200
    assert res_cd9.json()["is_correct"] is True
    assert res_cd9.json()["correct_answer"] == "C"

# 11. Coding-Decoding Full Bank Integrity and Difficulty Distribution
def test_11_coding_decoding_full_bank_integrity():
    from app.data.questions import QUESTIONS_DATA
    cd_questions = [q for q in QUESTIONS_DATA if q["topic"] == "Coding-Decoding"]
    assert len(cd_questions) >= 18

    easy = [q for q in cd_questions if q["difficulty"] == "Easy"]
    medium = [q for q in cd_questions if q["difficulty"] == "Medium"]
    hard = [q for q in cd_questions if q["difficulty"] == "Hard"]
    assert len(easy) >= 6
    assert len(medium) >= 6
    assert len(hard) >= 6

    ids = set()
    for q in cd_questions:
        assert q["id"] not in ids, f"Duplicate ID: {q['id']}"
        ids.add(q["id"])
        assert len(q["options"]) == 4, f"{q['id']} must have 4 options"
        option_texts = [opt["text"] for opt in q["options"]]
        assert len(set(option_texts)) == 4, f"{q['id']} options must be distinct: {option_texts}"
        option_ids = [opt["id"] for opt in q["options"]]
        assert option_ids == ["A", "B", "C", "D"]
        assert q["correct_answer"] in ["A", "B", "C", "D"]
        assert len(q["explanation"].strip()) > 10

# 12. Directional Sense Regression and Entire 72-Question Bank Integrity
def test_12_directional_sense_and_entire_bank_integrity():
    from app.data.questions import QUESTIONS_DATA

    # Regression test for ds-5
    res_ds5 = client.post("/api/questions/ds-5/submit", json={"selected_answer": "B"})
    assert res_ds5.status_code == 200
    assert res_ds5.json()["is_correct"] is True
    assert res_ds5.json()["correct_answer"] == "B"

    # Regression test for ds-6
    res_ds6 = client.post("/api/questions/ds-6/submit", json={"selected_answer": "A"})
    assert res_ds6.status_code == 200
    assert res_ds6.json()["is_correct"] is True
    assert res_ds6.json()["correct_answer"] == "A"

    # Full 450 questions integrity
    assert len(QUESTIONS_DATA) == 450
    seen_ids = set()
    for q in QUESTIONS_DATA:
        assert q["id"] not in seen_ids, f"Duplicate ID: {q['id']}"
        seen_ids.add(q["id"])
        assert len(q["question"].strip()) >= 15
        assert len(q["options"]) == 4
        option_texts = [opt["text"] for opt in q["options"]]
        assert len(set(option_texts)) == 4, f"Duplicate options in {q['id']}"
        option_ids = [opt["id"] for opt in q["options"]]
        assert option_ids == ["A", "B", "C", "D"]
        assert q["correct_answer"] in ["A", "B", "C", "D"]
        assert len(q["explanation"].strip()) >= 15

# 13. Syllogisms Medium 10 questions and all topic/difficulty combinations
def test_13_syllogisms_medium_10_and_all_topics_coverage():
    from app.data.questions import TOPICS_LIST

    # Specifically test the user's reported bug
    res_syl = client.get("/api/questions?topic=Syllogisms&difficulty=Medium&limit=10")
    assert res_syl.status_code == 200
    syl_questions = res_syl.json()
    assert len(syl_questions) == 10
    assert len(set(q["id"] for q in syl_questions)) == 10
    for q in syl_questions:
        assert q["topic"] == "Syllogisms"
        assert q["difficulty"] == "Medium"
        assert len(q["options"]) == 4

    # Test all 10 topics across all 3 difficulties with limit=10
    for topic in TOPICS_LIST:
        for diff in ["Easy", "Medium", "Hard"]:
            res = client.get(f"/api/questions?topic={topic}&difficulty={diff}&limit=10")
            assert res.status_code == 200, f"Failed for {topic} {diff}: {res.text}"
            qs = res.json()
            assert len(qs) == 10, f"Expected 10 questions for {topic} {diff}, got {len(qs)}"
            ids = set(q["id"] for q in qs)
            assert len(ids) == 10, f"Duplicate questions returned for {topic} {diff}"




