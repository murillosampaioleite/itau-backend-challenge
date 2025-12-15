from flask import jsonify, request
from typing import Tuple, Optional


def validate_json_request() -> Tuple[Optional[dict], Optional[tuple]]:
    """Valida se a requisição é JSON."""
    if not request.is_json:
        return None, (
            jsonify({
                'error': 'Bad Request',
                'message': 'Content-Type deve ser application/json',
                'statusCode': 400
            }),
            400
        )
    try:
        return request.get_json(), None
    except Exception:
        return None, (
            jsonify({
                'error': 'Bad Request',
                'message': 'Erro ao processar JSON da requisição',
                'statusCode': 400
            }),
            400
        )


def validate_password_field(data: dict) -> Tuple[Optional[str], Optional[tuple]]:
    """Valida o campo password."""
    if not data or 'password' not in data:
        return None, (
            jsonify({
                'error': 'Bad Request',
                'message': 'Campo "password" é obrigatório',
                'statusCode': 400
            }),
            400
        )
    
    password = data.get('password', '')
    
    if not isinstance(password, str):
        return None, (
            jsonify({
                'error': 'Bad Request',
                'message': 'Campo "password" deve ser uma string',
                'statusCode': 400
            }),
            400
        )
    
    return password, None
