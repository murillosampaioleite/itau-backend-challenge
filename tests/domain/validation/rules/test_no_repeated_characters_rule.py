"""
Testes unitários para NoRepeatedCharactersRule.
"""
import pytest

from src.domain.validation.rules.no_repeated_characters_rule import NoRepeatedCharactersRule


def test_should_return_false_when_password_contains_repeated_characters():
    """Testa se retorna False para senhas com caracteres repetidos."""
    rule = NoRepeatedCharactersRule()
    assert rule.is_valid("AbTp9!foo") is False
    assert rule.is_valid("AbTp9!foA") is False
    assert rule.is_valid("AAAbbbCc") is False

