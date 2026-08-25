"""Unit tests for Hivebox API"""
import pytest
import vcrpy
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

def test_metrics(client):
    """Test /metrics returns Prometheus format."""
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "python_info" in response.text
    assert "text/plain" in response.content_type

def test_temperature(client):
    """Test /temperature returns correct value"""
    response = client.get("/temperature")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert "average_temperature" in response.json

@vcr.use_cassette("cassettes/temperarture.yaml")
def test_temperature_response(client):
    """Integration test with recorded API responses"""
    response = client.get("/temperature")
    assert response.status_code in [200, 404]
    if response.status_code == 200:
        assert "average_temperature" in response.json
        assert "status" in response.json
        