import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_create_customer():
    payload = {
        "customer_id": "01234567890123456789012345678911",
        "customer_unique_id": "01234567890123456789012345678911",
        "customer_zip_code_prefix": "12345",
        "customer_city": "Test City",
        "customer_state": "TS"
    }

    response = client.post("/customers", json=payload)

    assert response.status_code == 200
    assert response.json() == payload