import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_order_payment():
    payload = {
        "order_id": "00010242fe8c5a6d1ba2dd792cb16214",
        "payment_sequential": 1,
        "payment_installments": 8,
        "payment_value": 13.29,
    }

    response = client.post("/order_payments", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload
