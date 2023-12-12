import pytest
from fastapi.testclient import TestClient

from api.app.main import app

client = TestClient(app)


def test_add_geolocation():
    payload = {
        "geolocation_zip_code_prefix": "01037",
        "geolocation_lat": "-23.54562128115268",
        "geolocation_lng": "-46.63929204800168",
    }

    response = client.post("/geolocation", json=payload)

    assert response.status_code == 200
