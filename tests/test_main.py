from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root_status_code():
    """Test that the root endpoint returns HTTP 200 status code."""
    response = client.get("/")
    assert response.status_code == 200

def test_read_root_response_format():
    """Test that the root endpoint returns valid JSON response."""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"
    
def test_read_root_response_content():
    """Test that the root endpoint returns the correct message."""
    response = client.get("/")
    json_response = response.json()
    assert json_response == {"message": "Hello, World!"}

def test_read_root_response_structure():
    """Test that the response has the expected structure."""
    response = client.get("/")
    json_response = response.json()
    assert "message" in json_response
    assert isinstance(json_response["message"], str)
    assert len(json_response) == 1
