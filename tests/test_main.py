from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root_status_code():
    """Test that GET request to root endpoint returns 200 status code."""
    response = client.get("/")
    assert response.status_code == 200

def test_read_root_response_format():
    """Test that GET request to root endpoint returns correct JSON message format."""
    response = client.get("/")
    assert response.json() == {"message": "Hello, World!"}
