"""
Testes unitários para ContainsLowerCaseRule.
"""
import pytest

from src.domain.validation.rules.contains_lowercase_rule import ContainsLowerCaseRule


def test_should_return_false_when_password_does_not_contain_lowercase():
    """Testa se retorna False para senhas sem letras minúsculas."""
    rule = ContainsLowerCaseRule()
    assert rule.is_valid("ABCDEFGH1!") is False

