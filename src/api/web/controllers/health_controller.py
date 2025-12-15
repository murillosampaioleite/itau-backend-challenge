"""Health check da aplicação."""
from flask import Blueprint, jsonify
from flasgger import swag_from

from src.api.web.config.swagger_config import get_health_check_swagger_spec

health_bp = Blueprint('health', __name__, url_prefix='/api/v1')


@health_bp.route('/health', methods=['GET'])
@swag_from(get_health_check_swagger_spec())
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'password-validator-api'
    }), 200
