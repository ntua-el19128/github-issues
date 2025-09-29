import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root_status_code():
    """Test that GET / returns HTTP 200 status code."""
    response = client.get("/")
    assert response.status_code == 200


def test_read_root_content_type():
    """Test that GET / returns JSON content type."""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"


def test_read_root_response_body():
    """Test that GET / returns correct JSON response body."""
    response = client.get("/")
    assert response.json() == {"message": "Hello, World!"}


def test_read_root_complete():
    """Test complete functionality of GET / endpoint."""
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "Hello, World!"}
