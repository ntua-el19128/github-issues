from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_read_root_response_json():
    response = client.get("/")
    assert response.json() == {"message": "Hello, World!"}


def test_read_root_accessible():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
