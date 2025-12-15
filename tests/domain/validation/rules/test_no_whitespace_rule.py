"""
Testes unitários para NoWhitespaceRule.
"""
import pytest

from src.domain.validation.rules.no_whitespace_rule import NoWhitespaceRule


def test_should_return_false_when_password_contains_whitespace():
    """Testa se retorna False para senhas com espaços em branco."""
    rule = NoWhitespaceRule()
    assert rule.is_valid("AbTp9 fok") is False


def test_should_return_true_when_password_does_not_contain_whitespace():
    """Testa se retorna True para senhas sem espaços."""
    rule = NoWhitespaceRule()
    assert rule.is_valid("AbTp9!fok") is True
