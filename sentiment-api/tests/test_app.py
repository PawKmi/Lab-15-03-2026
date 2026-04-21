from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_predict_valid_request_returns_prediction():
    response = client.post("/predict", json={"text": "I love this product"})
    assert response.status_code == 200

    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in {"negative", "neutral", "positive"}


def test_predict_empty_text():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422

    data = response.json()
    assert "detail" in data


def test_predict_missing_text():
    response = client.post("/predict", json={})
    assert response.status_code == 422

    data = response.json()
    assert "detail" in data