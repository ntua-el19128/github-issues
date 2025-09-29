import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint returns correct status and message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_root_content_type():
    """Test the root endpoint returns JSON content type."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
