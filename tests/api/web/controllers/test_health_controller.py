"""
Testes de integração para HealthController.
"""
import pytest
from flask import Flask

from app import app


@pytest.fixture
def client():
    """Cria um cliente de teste para a aplicação Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_should_return_healthy_status(client):
    """Testa se o endpoint de health check retorna status healthy."""
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'password-validator-api'
