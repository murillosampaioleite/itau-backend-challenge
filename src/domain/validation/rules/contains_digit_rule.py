"""Validação de dígitos."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class ContainsDigitRule(PasswordValidationRule):
    """Valida se contém pelo menos um dígito."""
    
    def is_valid(self, password: str) -> bool:
        return any(char.isdigit() for char in password)
    
    def get_description(self) -> str:
        return "A senha deve possuir ao menos 1 dígito"


