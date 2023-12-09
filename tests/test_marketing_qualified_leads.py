import pytest
from fastapi.testclient import TestClient

from api.app.main import app

client = TestClient(app)


def test_add_marketing_qualified_leads():
    payload = {
        "mql_id": "5420aad7fec3549a85876ba1c529bd84",
        "landing_page_id": "a8387c01a09e99ce014107505b92388c",
    }

    response = client.post("/marketing_qualified_leads", json=payload)

    assert response.status_code == 200
    # assert response.json() == payload
