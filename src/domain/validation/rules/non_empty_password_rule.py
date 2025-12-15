"""Validação de senha vazia."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class NonEmptyPasswordRule(PasswordValidationRule):
    """Valida se a senha não está vazia."""
    
    def is_valid(self, password: str) -> bool:
        return bool(password and password.strip())
    
    def get_description(self) -> str:
        return "A senha não pode estar vazia"
