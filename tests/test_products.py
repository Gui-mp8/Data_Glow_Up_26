import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_product():
    payload = {
        "product_id": "1e9e8ef04dbcff4541ed26657ea517e5",
    }

    response = client.post("/products", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload
