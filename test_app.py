from app import app
from fastapi.testclient import TestClient



def test_home():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"