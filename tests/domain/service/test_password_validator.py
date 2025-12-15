"""
Testes unitários para PasswordValidator.
"""
import pytest

from src.domain.service.password_validator import PasswordValidator
from src.domain.validation.rules.contains_digit_rule import ContainsDigitRule
from src.domain.validation.rules.contains_lowercase_rule import ContainsLowerCaseRule
from src.domain.validation.rules.contains_special_character_rule import ContainsSpecialCharacterRule
from src.domain.validation.rules.contains_uppercase_rule import ContainsUpperCaseRule
from src.domain.validation.rules.minimum_length_rule import MinimumLengthRule
from src.domain.validation.rules.no_repeated_characters_rule import NoRepeatedCharactersRule
from src.domain.validation.rules.no_whitespace_rule import NoWhitespaceRule
from src.domain.validation.rules.non_empty_password_rule import NonEmptyPasswordRule


def test_should_validate_all_test_cases_from_requirements():
    """Testa todos os casos de teste do enunciado."""
    validator = PasswordValidator()
    
    assert validator.is_valid("") is False
    assert validator.is_valid("aa") is False
    assert validator.is_valid("ab") is False
    assert validator.is_valid("AAAbbbCc") is False
    assert validator.is_valid("AbTp9!foo") is False
    assert validator.is_valid("AbTp9!foA") is False
    assert validator.is_valid("AbTp9 fok") is False
    assert validator.is_valid("AbTp9!fok") is True


def test_all_rules_should_return_true_for_valid_password():
    """Testa se todas as regras retornam True para uma senha válida."""
    valid_password = "AbTp9!fok"
    
    assert NonEmptyPasswordRule().is_valid(valid_password) is True
    assert MinimumLengthRule().is_valid(valid_password) is True
    assert ContainsDigitRule().is_valid(valid_password) is True
    assert ContainsLowerCaseRule().is_valid(valid_password) is True
    assert ContainsUpperCaseRule().is_valid(valid_password) is True
    assert ContainsSpecialCharacterRule().is_valid(valid_password) is True
    assert NoRepeatedCharactersRule().is_valid(valid_password) is True
    assert NoWhitespaceRule().is_valid(valid_password) is True


def test_validate_should_return_result_and_failed_rules():
    """Testa se o método validate retorna resultado e regras falhadas."""
    validator = PasswordValidator()
    
    is_valid, failed_rules = validator.validate("aa")
    assert is_valid is False
    assert len(failed_rules) > 0
    
    is_valid, failed_rules = validator.validate("AbTp9!fok")
    assert is_valid is True
    assert len(failed_rules) == 0


