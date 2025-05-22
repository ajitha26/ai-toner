
import pytest
from fastapi.testclient import TestClient
from app.main import app  # Updated import path to your actual app

client = TestClient(app)

def test_generate_endpoint():
    payload = {
        "user_id": "test_user",
        "query": "Explain blockchain"
    }
    response = client.post("/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "casual_response" in data
    assert "formal_response" in data

def test_history_endpoint():
    response = client.get("/history", params={"user_id": "test_user"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)