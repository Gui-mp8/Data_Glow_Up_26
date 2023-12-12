import pytest
from fastapi.testclient import TestClient

from api.app.main import app

client = TestClient(app)


def test_add_seller():
    payload = {
        "seller_id": "1e9e8ef04dbcff4541ed26657ea517e5",
    }

    response = client.post("/sellers", json=payload)

    assert response.status_code == 200
