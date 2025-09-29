import pytest
from fastapi.testclient import TestClient


def test_read_root_success(client):
    """Test that the root endpoint returns the expected response."""
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_read_root_response_format(client):
    """Test that the root endpoint returns proper JSON format."""
    response = client.get("/")
    
    assert response.headers["content-type"] == "application/json"
    
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "message" in json_data
    assert isinstance(json_data["message"], str)


def test_read_root_status_code(client):
    """Test that the root endpoint returns 200 status code."""
    response = client.get("/")
    assert response.status_code == 200


def test_read_root_message_content(client):
    """Test that the root endpoint returns the exact expected message."""
    response = client.get("/")
    json_data = response.json()
    assert json_data["message"] == "Hello, World!"


def test_read_root_method_not_allowed(client):
    """Test that non-GET methods return 405 Method Not Allowed."""
    response = client.post("/")
    assert response.status_code == 405
    
    response = client.put("/")
    assert response.status_code == 405
    
    response = client.delete("/")
    assert response.status_code == 405


def test_read_root_multiple_requests(client):
    """Test that multiple requests to root endpoint are consistent."""
    for _ in range(3):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}
