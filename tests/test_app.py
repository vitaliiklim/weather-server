import pytest
from ..app import app  # Залиште так, якщо запускаєте з кореневої директорії

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_weather(client):
    response = client.get('/weather')
    assert response.status_code == 200
    data = response.get_json()
    assert "temperature" in data
    assert "humidity" in data
    assert "status" in data
