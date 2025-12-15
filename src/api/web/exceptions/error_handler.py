"""Tratamento de erros da aplicação."""
from flask import Flask, jsonify

from src.api.web.constants import ERROR_MESSAGES, HTTP_STATUS


def register_error_handlers(app: Flask) -> None:
    """Registra handlers de erro."""
    @app.errorhandler(HTTP_STATUS['BAD_REQUEST'])
    def bad_request(error):
        """Erro 400."""
        message = (
            str(error.description) 
            if hasattr(error, 'description') and error.description 
            else ERROR_MESSAGES['BAD_REQUEST']
        )
        return jsonify({
            'error': ERROR_MESSAGES['BAD_REQUEST'],
            'message': message,
            'statusCode': HTTP_STATUS['BAD_REQUEST']
        }), HTTP_STATUS['BAD_REQUEST']
    
    @app.errorhandler(HTTP_STATUS['NOT_FOUND'])
    def not_found(error):
        """Erro 404."""
        return jsonify({
            'error': ERROR_MESSAGES['NOT_FOUND'],
            'message': ERROR_MESSAGES['ROUTE_NOT_FOUND'],
            'statusCode': HTTP_STATUS['NOT_FOUND']
        }), HTTP_STATUS['NOT_FOUND']
    
    @app.errorhandler(HTTP_STATUS['INTERNAL_ERROR'])
    def internal_error(error):
        """Erro 500."""
        return jsonify({
            'error': ERROR_MESSAGES['INTERNAL_ERROR'],
            'message': ERROR_MESSAGES['UNEXPECTED_ERROR'],
            'statusCode': HTTP_STATUS['INTERNAL_ERROR']
        }), HTTP_STATUS['INTERNAL_ERROR']
