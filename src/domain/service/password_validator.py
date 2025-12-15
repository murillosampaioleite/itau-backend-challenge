"""Validação de senhas conforme regras de negócio."""
from typing import List, Optional, Tuple

from src.domain.validation.password_validation_rule import PasswordValidationRule
from src.domain.validation.rules.contains_digit_rule import ContainsDigitRule
from src.domain.validation.rules.contains_lowercase_rule import ContainsLowerCaseRule
from src.domain.validation.rules.contains_special_character_rule import ContainsSpecialCharacterRule
from src.domain.validation.rules.contains_uppercase_rule import ContainsUpperCaseRule
from src.domain.validation.rules.minimum_length_rule import MinimumLengthRule
from src.domain.validation.rules.no_repeated_characters_rule import NoRepeatedCharactersRule
from src.domain.validation.rules.no_whitespace_rule import NoWhitespaceRule
from src.domain.validation.rules.non_empty_password_rule import NonEmptyPasswordRule


class PasswordValidator:
    """Valida senhas aplicando todas as regras de validação."""
    
    @staticmethod
    def _create_default_rules() -> List[PasswordValidationRule]:
        """Cria a lista padrão de regras de validação."""
        return [
            NonEmptyPasswordRule(),
            MinimumLengthRule(),
            ContainsDigitRule(),
            ContainsLowerCaseRule(),
            ContainsUpperCaseRule(),
            ContainsSpecialCharacterRule(),
            NoRepeatedCharactersRule(),
            NoWhitespaceRule()
        ]
    
    def __init__(self, rules: Optional[List[PasswordValidationRule]] = None):
        """Inicializa o validador. Usa regras padrão se não informar."""
        self.rules = rules if rules is not None else self._create_default_rules()
    
    def validate(self, password: str) -> Tuple[bool, List[str]]:
        """Valida a senha e retorna (is_valid, violations)."""
        violations = []
        for rule in self.rules:
            if not rule.is_valid(password):
                violations.append(rule.get_description())
        
        is_valid = len(violations) == 0
        return is_valid, violations
    
    def is_valid(self, password: str) -> bool:
        """Verifica se a senha atende todas as regras."""
        return all(rule.is_valid(password) for rule in self.rules)
    
    def get_failed_rules_descriptions(self, password: str) -> List[str]:
        """Retorna as descrições das regras que a senha não cumpriu."""
        return [rule.get_description() for rule in self.rules if not rule.is_valid(password)]


