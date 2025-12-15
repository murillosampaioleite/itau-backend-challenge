"""Validação de tamanho mínimo."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class MinimumLengthRule(PasswordValidationRule):
    """Valida tamanho mínimo da senha."""
    
    def __init__(self, minimum_length: int = 9):
        self.minimum_length = minimum_length
    
    def is_valid(self, password: str) -> bool:
        return len(password) >= self.minimum_length
    
    def get_description(self) -> str:
        return f"A senha deve possuir {self.minimum_length} ou mais caracteres"


