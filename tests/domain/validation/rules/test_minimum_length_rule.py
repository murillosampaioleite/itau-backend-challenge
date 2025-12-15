"""
Testes unitários para MinimumLengthRule.
"""
import pytest

from src.domain.validation.rules.minimum_length_rule import MinimumLengthRule


def test_should_return_false_when_password_has_less_than_9_characters():
    """Testa se retorna False para senhas com menos de 9 caracteres."""
    rule = MinimumLengthRule()
    assert rule.is_valid("aa") is False
    assert rule.is_valid("ab") is False


def test_should_return_true_when_password_has_at_least_9_characters():
    """Testa se retorna True para senhas com pelo menos 9 caracteres."""
    rule = MinimumLengthRule()
    assert rule.is_valid("AbTp9!fok") is True


