import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_add_closed_deals():
    payload = {
    "mql_id": "5420aad7fec3549a85876ba1c529bd84",
    "seller_id": "2c43fb513632d29b3b58df74816f1b06",
    "sdr_id": "a8387c01a09e99ce014107505b92388c",
    "sr_id": "4ef15afb4b2723d8f3d81e51ec7afefe",
    "won_date": "2018-02-26 19:58:54",
    "business_segment": "pet",
    "lead_type":"online_medium",
    "lead_behaviour_profile": "cat",
    "has_company":None,
    "has_gtin": None,
    "average_stock": None,
    "business_type": "reseller",
    "declared_product_catalog_size": None,
    "declared_monthly_revenue": 0.0
    }

    response = client.post("/closed_deals", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload