"""
Testes unitários para ContainsUpperCaseRule.
"""
import pytest

from src.domain.validation.rules.contains_uppercase_rule import ContainsUpperCaseRule


def test_should_return_false_when_password_does_not_contain_uppercase():
    """Testa se retorna False para senhas sem letras maiúsculas."""
    rule = ContainsUpperCaseRule()
    assert rule.is_valid("abcdefgh1!") is False


def test_should_return_true_when_password_contains_at_least_one_uppercase():
    """Testa se retorna True para senhas com ao menos uma letra maiúscula."""
    rule = ContainsUpperCaseRule()
    assert rule.is_valid("AbTp9!fok") is True


