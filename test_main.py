import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/api/hello')
    assert response.status_code == 200
    assert response.get_json() == {'hello': 'world'}

def test_hello_name(client):
    response = client.get('/api/hello/ben')
    assert response.status_code == 200
    assert response.get_json() == {'hello': 'ben'}