"""
Testes unitários para ContainsSpecialCharacterRule.
"""
import pytest

from src.domain.validation.rules.contains_special_character_rule import ContainsSpecialCharacterRule


def test_should_return_false_when_password_does_not_contain_valid_special_characters():
    """Testa se retorna False para senhas sem caracteres especiais válidos."""
    rule = ContainsSpecialCharacterRule()
    assert rule.is_valid("Abcdefgh1") is False


