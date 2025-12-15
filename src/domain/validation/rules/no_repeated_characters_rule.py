"""Validação de caracteres repetidos."""
from src.domain.validation.password_validation_rule import PasswordValidationRule


class NoRepeatedCharactersRule(PasswordValidationRule):
    """Valida se não há caracteres repetidos."""
    
    def is_valid(self, password: str) -> bool:
        char_set = set()
        for char in password:
            if char in char_set:
                return False
            char_set.add(char)
        
        return True
    
    def get_description(self) -> str:
        return "A senha não deve possuir caracteres repetidos"


