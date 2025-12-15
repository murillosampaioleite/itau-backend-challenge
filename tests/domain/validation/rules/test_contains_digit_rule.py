"""
Testes unitários para ContainsDigitRule.
"""
import pytest

from src.domain.validation.rules.contains_digit_rule import ContainsDigitRule


def test_should_return_false_when_password_does_not_contain_digits():
    """Testa se retorna False para senhas sem dígitos."""
    rule = ContainsDigitRule()
    assert rule.is_valid("Abcdefgh!") is False

