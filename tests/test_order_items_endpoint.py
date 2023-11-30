import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_order_item():
    payload = {
        "order_id": "00010242fe8c5a6d1ba2dd792cb16214",
        "order_item_id": 1,
        "product_id": "4244733e06e7ecb4970a6e2683c13e61",
        "seller_id": "48436dade18ac8b2bce089ec2a041202",
        "shipping_limit_date": "2017-09-19 09:45:35",
        "price": 58.90,
        "freight_value": 13.29,
    }

    response = client.post("/order_items", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload
