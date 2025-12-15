"""Validação de letras minúsculas."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class ContainsLowerCaseRule(PasswordValidationRule):
    """Valida se contém pelo menos uma letra minúscula."""
    
    def is_valid(self, password: str) -> bool:
        return any(char.islower() for char in password)
    
    def get_description(self) -> str:
        return "A senha deve possuir ao menos 1 letra minúscula"


