import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_order_review():
    payload = {
        "review_id": "00010242fe8c5a6d1ba2dd792cb16214",
        "order_id": "4244733e06e7ecb4970a6e2683c13e61",
        "review_creation_date": "2017-09-19 09:45:35",
        "review_answer_timestamp": "2017-09-19 09:45:35",
    }

    response = client.post("/order_reviews", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload
