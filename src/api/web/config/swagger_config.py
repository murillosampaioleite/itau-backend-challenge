"""Configurações do Swagger."""
from src.api.web.constants import RESPONSES

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger"
}

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "Itaú Backend Challenge - API de Validação de Senhas",
        "description": (
            "API RESTful para validação de senhas conforme regras de negócio especificadas. "
            "Esta API permite validar se uma senha atende a todos os critérios de segurança definidos."
        ),
        "version": "1.0.0",
        "contact": {
            "name": "API Support"
        }
    },
    "basePath": "/api/v1",
    "schemes": ["http", "https"],
    "tags": [
        {
            "name": "Health",
            "description": "Endpoints de verificação de status da aplicação"
        },
        {
            "name": "Passwords",
            "description": "Endpoints para validação de senhas"
        }
    ]
}

VALIDATION_RULES_DESCRIPTION = (
    "**Regras de validação:**\n"
    "- 9 ou mais caracteres\n"
    "- Ao menos 1 dígito\n"
    "- Ao menos 1 letra minúscula\n"
    "- Ao menos 1 letra maiúscula\n"
    "- Ao menos 1 caractere especial (!@#$%^&*()-+)\n"
    "- Sem caracteres repetidos\n"
    "- Sem espaços em branco"
)


def _get_base_swagger_spec() -> dict:
    """Especificação base do Swagger para validação de senha."""
    return {
        'tags': ['Passwords'],
        'summary': 'Valida uma senha',
        'description': f'Valida se uma senha atende a todas as regras de validação definidas.\n\n{VALIDATION_RULES_DESCRIPTION}',
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'required': ['password'],
                    'properties': {
                        'password': {
                            'type': 'string',
                            'description': 'Senha a ser validada'
                        }
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'Validação realizada com sucesso',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'isValid': {
                            'type': 'boolean',
                            'description': 'Indica se a senha é válida'
                        },
                        'violations': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            },
                            'description': 'Regras de validação que a senha não cumpriu. Array vazio quando isValid é true.'
                        }
                    }
                }
            },
            400: RESPONSES['BAD_REQUEST']
        }
    }


def get_health_check_swagger_spec() -> dict:
    """Especificação Swagger para o endpoint de health check."""
    return {
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
    }


def get_password_validation_swagger_spec() -> dict:
    """Especificação Swagger para o endpoint de validação de senha."""
    spec = _get_base_swagger_spec()
    spec['description'] = (
        f'Valida se uma senha atende a todas as regras de validação definidas.\n\n'
        f'{VALIDATION_RULES_DESCRIPTION}\n\n'
        '**Use os endpoints de exemplo abaixo para testar cada cenário diretamente!**'
    )
    spec['parameters'][0]['schema']['example'] = {'password': 'AbTp9!fok'}
    return spec


def _create_example_spec(password: str, description: str, summary: str) -> dict:
    """Cria uma especificação Swagger para um exemplo específico."""
    spec = _get_base_swagger_spec()
    spec['summary'] = summary
    spec['description'] = description
    spec['parameters'][0]['schema']['example'] = {'password': password}
    return spec


# Especificações para cada cenário de teste
EXAMPLES = [
    {
        'password': 'AbTp9!fok',
        'route_name': 'senha-valida',
        'summary': 'Senha válida',
        'description': 'Testa uma senha que atende todas as regras de validação.\n\n**Senha:** `AbTp9!fok`\n\n**Resultado esperado:** `{"isValid": true, "violations": []}`'
    },
    {
        'password': '',
        'route_name': 'senha-vazia',
        'summary': 'Senha vazia',
        'description': 'Testa uma senha vazia (inválida).\n\n**Senha:** `""`\n\n**Resultado esperado:** `{"isValid": false, "violations": [...]}`'
    },
    {
        'password': 'aa',
        'route_name': 'senha-muito-curta',
        'summary': 'Senha muito curta',
        'description': 'Testa uma senha com menos de 9 caracteres (inválida).\n\n**Senha:** `aa`\n\n**Resultado esperado:** `{"isValid": false, "violations": [...]}`'
    },
    {
        'password': 'ab',
        'route_name': 'senha-sem-digito',
        'summary': 'Senha sem dígito',
        'description': 'Testa uma senha sem dígito (inválida).\n\n**Senha:** `ab`\n\n**Resultado esperado:** `{"isValid": false, "violations": [...]}`'
    },
    {
        'password': 'AAAbbbCc',
        'route_name': 'senha-com-repeticao',
        'summary': 'Senha com caracteres repetidos',
        'description': 'Testa uma senha com caracteres repetidos (inválida).\n\n**Senha:** `AAAbbbCc`\n\n**Resultado esperado:** `{"isValid": false, "violations": [...]}`'
    },
    {
        'password': 'AbTp9!foo',
        'route_name': 'senha-repeticao-o',
        'summary': 'Senha com caractere "o" repetido',
        'description': 'Testa uma senha com o caractere "o" repetido (inválida).\n\n**Senha:** `AbTp9!foo`\n\n**Resultado esperado:** `{"isValid": false, "violations": [...]}`'
    },
    {
        'password': 'AbTp9!foA',
        'route_name': 'senha-repeticao-A',
        'summary': 'Senha com caractere "A" repetido',
        'description': 'Testa uma senha com o caractere "A" repetido (inválida).\n\n**Senha:** `AbTp9!foA`\n\n**Resultado esperado:** `{"isValid": false, "violations": [...]}`'
    },
    {
        'password': 'AbTp9 fok',
        'route_name': 'senha-com-espaco',
        'summary': 'Senha com espaço em branco',
        'description': 'Testa uma senha com espaço em branco (inválida).\n\n**Senha:** `AbTp9 fok`\n\n**Resultado esperado:** `{"isValid": false, "violations": [...]}`'
    }
]


def get_example_swagger_specs() -> list:
    """Retorna lista de especificações Swagger para cada exemplo."""
    return [
        _create_example_spec(
            password=ex['password'],
            description=ex['description'],
            summary=ex['summary']
        )
        for ex in EXAMPLES
    ]


def register_example_endpoints(blueprint, handler_function):
    """Registra todos os endpoints de exemplo no blueprint."""
    example_specs = get_example_swagger_specs()
    
    def create_example_endpoint(route: str, spec_data: dict, handler_name: str):
        """Cria um endpoint de exemplo."""
        from flasgger import swag_from
        
        @blueprint.route(route, methods=['POST'])
        @swag_from(spec_data)
        def handler():
            """Valida uma senha usando exemplo pré-definido."""
            return handler_function()
        
        handler.__name__ = handler_name
        return handler
    
    # Registrar todos os endpoints de exemplo
    for example, spec in zip(EXAMPLES, example_specs):
        route_name = f'/validation/{example["route_name"]}'
        endpoint_name = f'validate_password_{example["route_name"].replace("-", "_")}'
        create_example_endpoint(route_name, spec, endpoint_name)
