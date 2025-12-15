"""Health check da aplicação."""
from flask import Blueprint, jsonify
from flasgger import swag_from

health_bp = Blueprint('health', __name__, url_prefix='/api/v1')


@health_bp.route('/health', methods=['GET'])
@swag_from({
    'tags': ['Health'],
    'summary': 'Verifica o status da aplicação',
    'description': 'Endpoint para verificar se a aplicação está funcionando corretamente',
    'responses': {
        200: {
            'description': 'Aplicação está funcionando corretamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'healthy'
                    },
                    'service': {
                        'type': 'string',
                        'example': 'password-validator-api'
                    }
                }
            }
        }
    }
})
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'password-validator-api'
    }), 200
