import pytest
from fastapi.testclient import TestClient

from api.app.main import app

client = TestClient(app)


def test_add_order():
    payload = {
        "order_id": "00010242fe8c5a6d1ba2dd792cb16214",
        "customer_id": "4244733e06e7ecb4970a6e2683c13e61",
        "order_status": "PENDING",
        "order_purchase_timestamp": "2017-09-19 09:45:35",
        "order_delivered_carrier_date": "2017-09-19 09:45:35",
        "order_delivered_customer_date": "2017-09-19 09:45:35",
        "order_estimated_delivery_date": "2017-09-19 09:45:35",
    }

    response = client.post("/orders", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload
