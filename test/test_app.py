# tests/test_app.py
import pytest 
from app import app as flask_app

@pytest.fixture
def client():
    # ... (código de configuración del cliente) ...
    with flask_app.test_client() as client:
        yield client

def test_home_route_status(client):
    response = client.get('/')
    assert response.status_code == 200