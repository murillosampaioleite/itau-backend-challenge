"""Interface para regras de validação de senha."""
from abc import ABC, abstractmethod


class PasswordValidationRule(ABC):
    """Interface para regras de validação."""
    
    @abstractmethod
    def is_valid(self, password: str) -> bool:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass


