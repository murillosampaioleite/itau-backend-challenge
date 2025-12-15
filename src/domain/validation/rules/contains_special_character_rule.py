"""Validação de caracteres especiais."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class ContainsSpecialCharacterRule(PasswordValidationRule):
    """Valida se contém pelo menos um caractere especial."""
    
    SPECIAL_CHARACTERS = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'}
    
    def is_valid(self, password: str) -> bool:
        return any(char in self.SPECIAL_CHARACTERS for char in password)
    
    def get_description(self) -> str:
        return "A senha deve possuir ao menos 1 caractere especial (!@#$%^&*()-+)"


