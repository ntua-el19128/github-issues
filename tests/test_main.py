from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint returns correct response."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_root_status_code():
    """Test the root endpoint returns 200 status code."""
    response = client.get("/")
    assert response.status_code == 200

def test_read_root_response_format():
    """Test the root endpoint returns valid JSON."""
    response = client.get("/")
    assert response.headers["content-type"] == "application/json"
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "message" in json_data
