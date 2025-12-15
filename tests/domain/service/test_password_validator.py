"""
Testes unitários para PasswordValidator.
"""
import pytest

from src.domain.service.password_validator import PasswordValidator


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


def test_validate_should_return_result_and_failed_rules():
    """Testa se o método validate retorna resultado e regras falhadas."""
    validator = PasswordValidator()
    
    is_valid, failed_rules = validator.validate("aa")
    assert is_valid is False
    assert len(failed_rules) > 0
    
    is_valid, failed_rules = validator.validate("AbTp9!fok")
    assert is_valid is True
    assert len(failed_rules) == 0


