"""
Testes unitários para NonEmptyPasswordRule.
"""
import pytest

from src.domain.validation.rules.non_empty_password_rule import NonEmptyPasswordRule


def test_should_return_false_for_empty_password():
    """Testa se retorna False para senha vazia."""
    rule = NonEmptyPasswordRule()
    assert rule.is_valid("") is False

