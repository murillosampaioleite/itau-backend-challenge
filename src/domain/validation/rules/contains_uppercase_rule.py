"""Validação de letras maiúsculas."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class ContainsUpperCaseRule(PasswordValidationRule):
    """Valida se contém pelo menos uma letra maiúscula."""
    
    def is_valid(self, password: str) -> bool:
        return any(char.isupper() for char in password)
    
    def get_description(self) -> str:
        return "A senha deve possuir ao menos 1 letra maiúscula"


