"""
Testes unitários para ContainsDigitRule.
"""
import pytest

from src.domain.validation.rules.contains_digit_rule import ContainsDigitRule


def test_should_return_false_when_password_does_not_contain_digits():
    """Testa se retorna False para senhas sem dígitos."""
    rule = ContainsDigitRule()
    assert rule.is_valid("Abcdefgh!") is False


def test_should_return_true_when_password_contains_at_least_one_digit():
    """Testa se retorna True para senhas com ao menos um dígito."""
    rule = ContainsDigitRule()
    assert rule.is_valid("AbTp9!fok") is True
