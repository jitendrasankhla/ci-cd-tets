from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hi"}

def test_read_root_invalid_method():
    response = client.post("/")
    assert response.status_code == 405  # Method Not Allowed

def test_read_invalid_endpoint():
    response = client.get("/invalid")
    print()
    assert response.status_code == 404  # Not Found



