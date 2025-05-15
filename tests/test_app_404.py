import pytest
from app.app import app  

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_404_route(client):
    response = client.get("/non-existent-endpoint")
    assert response.status_code == 404
    assert b"Not Found" in response.data  # Optional: check default error message
