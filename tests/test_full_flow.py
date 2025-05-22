from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_full_user_flow():
    query = "Define blockchain"
    user_id = "testuser"

    # Step 1: Generate response
    post_res = client.post("/generate", json={"user_id": user_id, "query": query})
    assert post_res.status_code == 200
    data = post_res.json()
    assert "casual_response" in data and "formal_response" in data

    # Step 2: Fetch history
    get_res = client.get("/history", params={"user_id": user_id})
    assert get_res.status_code == 200
    history = get_res.json()
    assert any(item["query"] == query for item in history)