"""
Testes unitários para ContainsSpecialCharacterRule.
"""
import pytest

from src.domain.validation.rules.contains_special_character_rule import ContainsSpecialCharacterRule


def test_should_return_false_when_password_does_not_contain_valid_special_characters():
    """Testa se retorna False para senhas sem caracteres especiais válidos."""
    rule = ContainsSpecialCharacterRule()
    assert rule.is_valid("Abcdefgh1") is False


def test_should_return_true_when_password_contains_at_least_one_valid_special_character():
    """Testa se retorna True para senhas com ao menos um caractere especial válido."""
    rule = ContainsSpecialCharacterRule()
    assert rule.is_valid("AbTp9!fok") is True


