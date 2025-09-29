import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root_status_code():
    """Test that the root endpoint returns status code 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_read_root_response_body():
    """Test that the root endpoint returns the correct JSON body."""
    response = client.get("/")
    assert response.json() == {"message": "Hello, World!"}


def test_read_root_endpoint_availability():
    """Test that the root endpoint is available and returns valid JSON."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], str)
