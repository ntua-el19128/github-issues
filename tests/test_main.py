from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    """Test GET / returns correct JSON response with 200 status code."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_root_response_format():
    """Test GET / returns proper JSON content type."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert isinstance(response.json(), dict)
    assert "message" in response.json()

def test_post_root_not_allowed():
    """Test POST / returns 405 Method Not Allowed."""
    response = client.post("/")
    assert response.status_code == 405

def test_put_root_not_allowed():
    """Test PUT / returns 405 Method Not Allowed."""
    response = client.put("/")
    assert response.status_code == 405

def test_delete_root_not_allowed():
    """Test DELETE / returns 405 Method Not Allowed."""
    response = client.delete("/")
    assert response.status_code == 405

def test_patch_root_not_allowed():
    """Test PATCH / returns 405 Method Not Allowed."""
    response = client.patch("/")
    assert response.status_code == 405
