import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_product_category_name_translation():
    payload = {
        "product_category_name": "alguma coisa",
        "product_category_name_english": "something",
    }

    response = client.post("/product_category_name_translation", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload
