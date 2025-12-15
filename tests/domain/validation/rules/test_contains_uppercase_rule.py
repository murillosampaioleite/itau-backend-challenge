"""
Testes unitários para ContainsUpperCaseRule.
"""
import pytest

from src.domain.validation.rules.contains_uppercase_rule import ContainsUpperCaseRule


def test_should_return_false_when_password_does_not_contain_uppercase():
    """Testa se retorna False para senhas sem letras maiúsculas."""
    rule = ContainsUpperCaseRule()
    assert rule.is_valid("abcdefgh1!") is False

