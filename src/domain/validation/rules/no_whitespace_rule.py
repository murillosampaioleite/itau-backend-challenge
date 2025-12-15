"""Validação de espaços em branco."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class NoWhitespaceRule(PasswordValidationRule):
    """Valida se não contém espaços."""
    
    def is_valid(self, password: str) -> bool:
        return ' ' not in password
    
    def get_description(self) -> str:
        return "A senha não deve conter espaços em branco"
