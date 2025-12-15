"""Testes de integração do controller de validação de senhas."""
import pytest
from flask import Flask

from app import app


@pytest.fixture
def client():
    """Cliente de teste Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_should_validate_all_test_cases_from_requirements_via_api(client):
    """Valida todos os casos de teste do enunciado via API."""
    test_cases = [
        ("", False),
        ("aa", False),
        ("ab", False),
        ("AAAbbbCc", False),
        ("AbTp9!foo", False),
        ("AbTp9!foA", False),
        ("AbTp9 fok", False),
        ("AbTp9!fok", True)
    ]
    
    for password, expected in test_cases:
        response = client.post(
            '/api/v1/passwords/validation',
            json={'password': password},
            content_type='application/json'
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data['isValid'] == expected
        assert 'violations' in data
        assert isinstance(data['violations'], list)

