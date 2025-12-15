"""
Testes unitários para ContainsLowerCaseRule.
"""
import pytest

from src.domain.validation.rules.contains_lowercase_rule import ContainsLowerCaseRule


def test_should_return_false_when_password_does_not_contain_lowercase():
    """Testa se retorna False para senhas sem letras minúsculas."""
    rule = ContainsLowerCaseRule()
    assert rule.is_valid("ABCDEFGH1!") is False


def test_should_return_true_when_password_contains_at_least_one_lowercase():
    """Testa se retorna True para senhas com ao menos uma letra minúscula."""
    rule = ContainsLowerCaseRule()
    assert rule.is_valid("AbTp9!fok") is True


