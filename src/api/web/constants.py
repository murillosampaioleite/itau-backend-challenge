"""Constantes utilizadas na camada web."""

# Mensagens de erro
ERROR_MESSAGES = {
    'BAD_REQUEST': 'Bad Request',
    'NOT_FOUND': 'Not Found',
    'INTERNAL_ERROR': 'Internal Server Error',
    'INVALID_JSON': 'Content-Type deve ser application/json',
    'MISSING_PASSWORD': 'Campo "password" é obrigatório',
    'INVALID_PASSWORD_TYPE': 'Campo "password" deve ser uma string',
    'ROUTE_NOT_FOUND': 'A rota solicitada não existe',
    'UNEXPECTED_ERROR': 'Ocorreu um erro inesperado no servidor'
}

# Códigos de status HTTP
HTTP_STATUS = {
    'OK': 200,
    'BAD_REQUEST': 400,
    'NOT_FOUND': 404,
    'INTERNAL_ERROR': 500
}

# Respostas padrão
RESPONSES = {
    'SUCCESS': {
        'description': 'Operação realizada com sucesso'
    },
    'BAD_REQUEST': {
        'description': 'Erro na requisição',
        'schema': {
            'type': 'object',
            'properties': {
                'error': {'type': 'string', 'example': 'Bad Request'},
                'message': {'type': 'string'},
                'statusCode': {'type': 'integer', 'example': 400}
            }
        }
    }
}
