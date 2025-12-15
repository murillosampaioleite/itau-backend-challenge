"""Controller REST para validação de senhas."""
from flask import Blueprint, jsonify
from flasgger import swag_from

from src.domain.service.password_validator import PasswordValidator
from src.api.web.utils.request_validator import validate_json_request, validate_password_field
from src.api.web.config.swagger_config import (
    get_password_validation_swagger_spec,
    register_example_endpoints
)

password_bp = Blueprint('passwords', __name__, url_prefix='/api/v1/passwords')


def _get_validator() -> PasswordValidator:
    """Cria instância do validador."""
    return PasswordValidator()


def _validate_password_handler():
    """Handler comum para validação de senha."""
    data, error = validate_json_request()
    if error:
        return error
    
    password, error = validate_password_field(data)
    if error:
        return error
    
    validator = _get_validator()
    is_valid, violations = validator.validate(password)
    
    return jsonify({
        'isValid': is_valid,
        'violations': violations
    }), 200


@password_bp.route('/validation', methods=['POST'])
@swag_from(get_password_validation_swagger_spec())
def validate_password():
    """Valida uma senha."""
    return _validate_password_handler()


# Registrar todos os endpoints de exemplo
register_example_endpoints(password_bp, _validate_password_handler)
