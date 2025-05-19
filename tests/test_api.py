from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_post_data():
    data = {
        "sensor_id": 1,
        "timestamp": "2024-05-16T12:00:00Z",
        "temperature": 25.0,
        "pressure": 101.0
    }
    response = client.post("/data", json=data)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}