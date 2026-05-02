from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict_valid():
    data = {
        "credit_score": 650,
        "gender": "Male",
        "age": 35,
        "tenure": 5,
        "balance": 50000.0,
        "products_number": 2,
        "credit_card": 1,
        "active_member": 1,
        "estimated_salary": 60000.0
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert "churn_prediction" in response.json()

def test_predict_invalid():
    data = {
        "credit_score": -1,  # inválido
        "gender": "Alien",
        "age": 10,
        "tenure": 5,
        "balance": 50000.0,
        "products_number": 2,
        "credit_card": 1,
        "active_member": 1,
        "estimated_salary": 60000.0
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 422
