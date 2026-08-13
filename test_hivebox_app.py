"""Unit tests for Hivebox API"""
import pytest
from hivebox_app import app

@pytest.fixture(name="client")
def client_ficture():
    """Create a test client"""
    with app.test_client() as client:
        yield client

def test_version(client):
    """Test /version returns correct version"""
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json =={"version": "0.0.1"}

def test_temperature(client):
    """Test /temperature returns correct value"""
    response = client.get("/temperature")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert "average_temperature" in response.json
