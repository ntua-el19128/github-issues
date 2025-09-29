from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root_status_code():
    """Test that GET / returns status code 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_read_root_response_format():
    """Test that GET / returns correct JSON response format"""
    response = client.get("/")
    assert response.json() == {"message": "Hello, World!"}

def test_read_root_response_headers():
    """Test that GET / returns correct content type"""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"

def test_read_root_response_structure():
    """Test that GET / response has expected structure"""
    response = client.get("/")
    json_response = response.json()
    assert isinstance(json_response, dict)
    assert "message" in json_response
    assert isinstance(json_response["message"], str)

def test_read_root_method_not_allowed():
    """Test that POST / returns method not allowed"""
    response = client.post("/")
    assert response.status_code == 405

def test_read_root_multiple_requests():
    """Test that multiple requests to / work consistently"""
    for _ in range(3):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}
