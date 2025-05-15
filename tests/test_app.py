# import requests

# def test_healthz():
#     r = requests.get("http://localhost:5000/healthz")
#     assert r.status_code == 200


import pytest
from app.app import app  # Replace with the name of your Python file without `.py`

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_healthz(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.data.decode() == "OK"
