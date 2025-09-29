from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root_status_code():
    """Test that root endpoint returns HTTP 200 status code."""
    response = client.get("/")
    assert response.status_code == 200


def test_read_root_response_content():
    """Test that root endpoint returns correct JSON payload."""
    response = client.get("/")
    assert response.json() == {"message": "Hello, World!"}
