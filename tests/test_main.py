import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root_success():
    """Test that the root endpoint returns 200 status and correct JSON response."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_root_content_type():
    """Test that the root endpoint returns correct content type."""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

def test_read_root_response_structure():
    """Test that the response has the expected JSON structure."""
    response = client.get("/")
    json_response = response.json()
    assert isinstance(json_response, dict)
    assert "message" in json_response
    assert isinstance(json_response["message"], str)

def test_unsupported_http_methods():
    """Test that unsupported HTTP methods return 405 Method Not Allowed."""
    response = client.post("/")
    assert response.status_code == 405
    
    response = client.put("/")
    assert response.status_code == 405
    
    response = client.delete("/")
    assert response.status_code == 405
    
    response = client.patch("/")
    assert response.status_code == 405

def test_root_endpoint_with_query_parameters():
    """Test that the root endpoint ignores query parameters."""
    response = client.get("/?param=value")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_root_endpoint_multiple_requests():
    """Test that multiple requests to root endpoint are consistent."""
    for _ in range(3):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}
