# Itaú Backend Challenge - Validador de Senhas

API RESTful desenvolvida em Python para validação de senhas conforme regras de negócio específicas. A solução foi implementada utilizando Flask, seguindo princípios de arquitetura limpa e SOLID para garantir manutenibilidade e testabilidade.

## Visão Geral

Esta aplicação expõe endpoints REST para validação de senhas, verificando se uma senha atende a todas as regras de segurança definidas. A API retorna não apenas se a senha é válida ou não, mas também lista todas as regras que foram violadas, facilitando o feedback ao usuário.

## Requisitos de Validação

Uma senha é considerada válida quando atende simultaneamente a todas as seguintes condições:

1. **Nove ou mais caracteres**: A senha deve possuir no mínimo 9 caracteres
2. **Ao menos 1 dígito**: A senha deve conter pelo menos um número (0-9)
3. **Ao menos 1 letra minúscula**: A senha deve conter pelo menos uma letra minúscula (a-z)
4. **Ao menos 1 letra maiúscula**: A senha deve conter pelo menos uma letra maiúscula (A-Z)
5. **Ao menos 1 caractere especial**: A senha deve conter pelo menos um dos seguintes caracteres especiais: `!@#$%^&*()-+`
6. **Sem caracteres repetidos**: A senha não pode conter caracteres repetidos
7. **Sem espaços em branco**: Espaços em branco não são considerados caracteres válidos

### Exemplos de Validação

- `IsValid("")` → `false` (senha vazia)
- `IsValid("aa")` → `false` (menos de 9 caracteres)
- `IsValid("ab")` → `false` (menos de 9 caracteres e sem dígito)
- `IsValid("AAAbbbCc")` → `false` (caracteres repetidos)
- `IsValid("AbTp9!foo")` → `false` (caractere 'o' repetido)
- `IsValid("AbTp9!foA")` → `false` (caractere 'A' repetido)
- `IsValid("AbTp9 fok")` → `false` (contém espaço)
- `IsValid("AbTp9!fok")` → `true` (atende todas as regras)

## Estrutura do Projeto

O projeto segue uma arquitetura em camadas, separando responsabilidades entre a camada de apresentação (API), domínio (regras de negócio) e testes.

```
itau-backend-challenge/
├── app.py                          # Ponto de entrada da aplicação Flask
├── Dockerfile                      # Configuração da imagem Docker
├── docker-compose.yml              # Orquestração dos containers
├── requirements.txt                # Dependências Python do projeto
├── pytest.ini                     # Configuração do pytest
├── README.md                       # Documentação do projeto
│
├── src/                            # Código fonte da aplicação
│   ├── api/                        # Camada de apresentação (API)
│   │   └── web/
│   │       ├── config/             # Configurações da aplicação
│   │       │   └── swagger_config.py    # Configuração do Swagger/OpenAPI
│   │       ├── controllers/        # Controllers REST
│   │       │   ├── health_controller.py  # Endpoint de health check
│   │       │   └── password_controller.py # Endpoint de validação de senhas
│   │       ├── exceptions/         # Tratamento de erros
│   │       │   └── error_handler.py     # Handlers de exceções HTTP
│   │       ├── utils/              # Utilitários da camada web
│   │       │   └── request_validator.py # Validação de requisições HTTP
│   │       └── constants.py        # Constantes da camada web
│   │
│   └── domain/                     # Camada de domínio (regras de negócio)
│       ├── service/                # Serviços de domínio
│       │   └── password_validator.py    # Validador principal de senhas
│       └── validation/             # Regras de validação
│           ├── password_validation_rule.py  # Interface abstrata para regras
│           └── rules/               # Implementações das regras
│               ├── contains_digit_rule.py
│               ├── contains_lowercase_rule.py
│               ├── contains_special_character_rule.py
│               ├── contains_uppercase_rule.py
│               ├── minimum_length_rule.py
│               ├── no_repeated_characters_rule.py
│               ├── no_whitespace_rule.py
│               └── non_empty_password_rule.py
│
└── tests/                          # Testes automatizados
    ├── api/                        # Testes da camada API
    │   └── web/
    │       └── controllers/
    │           ├── test_health_controller.py
    │           └── test_password_controller.py
    └── domain/                     # Testes da camada de domínio
        ├── service/
        │   └── test_password_validator.py
        └── validation/
            └── rules/               # Testes unitários de cada regra
                ├── test_contains_digit_rule.py
                ├── test_contains_lowercase_rule.py
                ├── test_contains_special_character_rule.py
                ├── test_contains_uppercase_rule.py
                ├── test_minimum_length_rule.py
                ├── test_no_repeated_characters_rule.py
                ├── test_no_whitespace_rule.py
                └── test_non_empty_password_rule.py
```

### Descrição das Camadas

**Camada de API (`src/api/web/`)**
- `controllers/`: Define os endpoints REST e orquestra as requisições HTTP
- `config/`: Configurações da aplicação, incluindo Swagger
- `exceptions/`: Tratamento centralizado de erros HTTP
- `utils/`: Utilitários para validação de requisições e outros helpers

**Camada de Domínio (`src/domain/`)**
- `service/`: Contém a lógica de negócio principal (PasswordValidator)
- `validation/`: Define as regras de validação através do padrão Strategy
- Cada regra implementa a interface `PasswordValidationRule`, permitindo fácil extensão

**Camada de Testes (`tests/`)**
- Estrutura espelha a organização do código fonte
- Testes unitários para cada regra de validação
- Testes de integração para os controllers
- Cobertura completa dos casos de uso do desafio

## Executando a Aplicação

### Pré-requisitos

- Docker
- Docker Compose

### Execução com Docker Compose

A forma mais simples de executar a aplicação é utilizando Docker Compose, que configura automaticamente o ambiente e expõe a aplicação na porta 8080.

1. Clone o repositório:
```bash
git clone https://github.com/murillosampaioleite/itau-backend-challenge.git
cd itau-backend-challenge
```

2. Execute a aplicação:
```bash
docker-compose up -d --build
```

A aplicação estará disponível em `http://localhost:8080` após a inicialização.

### Comandos Úteis do Docker Compose

Parar a aplicação:
```bash
docker-compose down
```

Visualizar logs em tempo real:
```bash
docker-compose logs -f
```

Reconstruir a imagem do zero (sem cache):
```bash
docker-compose build --no-cache
```

Acessar o shell do container:
```bash
docker-compose exec password-validator-api bash
```

### Execução Local (sem Docker)

Caso prefira executar localmente sem Docker:

1. Instale Python 3.11 ou superior
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python app.py
```

## Executando os Testes

Os testes foram desenvolvidos utilizando pytest e seguem a mesma estrutura organizacional do código fonte. A configuração do pytest está definida em `pytest.ini`.

### Executar Testes no Container Docker

Com a aplicação rodando via Docker Compose, execute os testes dentro do container:

```bash
docker-compose exec password-validator-api pytest
```

### Executar Testes Localmente

Se estiver executando localmente, ative o ambiente virtual e execute:

```bash
pytest
```

### Estrutura dos Testes

Os testes estão organizados em três categorias:

1. **Testes Unitários de Regras** (`tests/domain/validation/rules/`): Cada regra de validação possui seu próprio arquivo de teste, validando comportamento isolado
2. **Testes do Validador** (`tests/domain/service/`): Testam a integração entre múltiplas regras e o comportamento do PasswordValidator
3. **Testes de Integração** (`tests/api/web/controllers/`): Testam os endpoints HTTP end-to-end, incluindo validação de requisições e respostas

Todos os casos de teste do enunciado do desafio estão cobertos pelos testes de integração.

### Resultado dos Testes

Abaixo está a evidência de que todos os testes estão passando com sucesso:

![Resultado dos Testes](https://freeimage.host/i/farVaoB)

## Documentação Swagger

A aplicação inclui documentação interativa da API através do Swagger UI, facilitando testes e exploração dos endpoints sem necessidade de ferramentas externas.

### Acessando o Swagger

Com a aplicação rodando, acesse:

```
http://localhost:8080/swagger
```

### Como Usar o Swagger

1. Inicie a aplicação com `docker-compose up --build`
2. Abra seu navegador e acesse `http://localhost:8080/swagger`
3. Expanda o endpoint desejado na interface
4. Clique em "Try it out" para habilitar a edição
5. Preencha os parâmetros necessários no body da requisição
6. Clique em "Execute" para enviar a requisição
7. Visualize a resposta, código de status HTTP e headers retornados

## Endpoints da API

### Health Check

Verifica o status da aplicação.

**GET** `/api/v1/health`

**Resposta (200 OK):**
```json
{
  "status": "healthy",
  "service": "password-validator-api"
}
```

### Validação de Senha

Valida se uma senha atende a todas as regras de validação definidas.

**POST** `/api/v1/passwords/validation`

**Headers:**
```
Content-Type: application/json
```

**Body:**
```json
{
  "password": "AbTp9!fok"
}
```

**Resposta de Sucesso (200 OK):**
```json
{
  "isValid": true,
  "violations": []
}
```

**Resposta de Senha Inválida (200 OK):**
```json
{
  "isValid": false,
  "violations": [
    "A senha deve ter no mínimo 9 caracteres",
    "A senha deve conter ao menos um dígito"
  ]
}
```

**Exemplo de Requisição com cURL:**
```bash
curl -X POST http://localhost:8080/api/v1/passwords/validation \
  -H "Content-Type: application/json" \
  -d '{"password": "AbTp9!fok"}'
```

### Tratamento de Erros

A API retorna códigos de status HTTP apropriados seguindo padrões RESTful:

- **200 OK**: Validação realizada com sucesso (independente de ser válida ou não)
- **400 Bad Request**: Erro na requisição
  - Campo `password` ausente
  - Content-Type não é `application/json`
  - Campo `password` não é uma string

**Exemplo de Resposta de Erro (400):**
```json
{
  "error": "Bad Request",
  "message": "Campo \"password\" é obrigatório",
  "statusCode": 400
}
```

## Arquitetura e Decisões de Design

### Princípios Aplicados

A solução foi desenvolvida seguindo os princípios SOLID e Clean Architecture:

- **Single Responsibility**: Cada classe tem uma única responsabilidade bem definida
- **Open/Closed**: Novas regras de validação podem ser adicionadas sem modificar código existente
- **Dependency Inversion**: A camada de API depende de abstrações (interfaces) do domínio
- **Separation of Concerns**: Separação clara entre camadas de apresentação, domínio e testes

### Padrões de Design Utilizados

**Strategy Pattern**: As regras de validação implementam a interface `PasswordValidationRule`, permitindo que o `PasswordValidator` aplique diferentes estratégias de validação de forma flexível.

**Factory Pattern**: O `PasswordValidator` possui um método factory (`_create_default_rules()`) para criar a lista padrão de regras, mas também aceita regras customizadas via construtor.

**Template Method**: A estrutura comum de validação é definida na interface, enquanto cada regra implementa sua lógica específica.

### Premissas Assumidas

1. **Espaços em branco**: Espaços são considerados caracteres inválidos. Uma senha com espaços é automaticamente rejeitada, mesmo que atenda às outras regras.

2. **Caracteres especiais**: Apenas os caracteres especificados (`!@#$%^&*()-+`) são considerados válidos. Outros caracteres especiais não são aceitos.

3. **Case sensitivity**: A validação diferencia letras maiúsculas e minúsculas.

4. **API REST**: A solução expõe uma API REST seguindo convenções RESTful, com versionamento da API (`/api/v1/`).

5. **Resposta de validação**: A API sempre retorna status 200 para validações bem-sucedidas, diferenciando senhas válidas e inválidas através do campo `isValid` no body da resposta.

## Tecnologias Utilizadas

- **Python 3.14**: Linguagem de programação
- **Flask 3.1.2**: Framework web minimalista
- **Flasgger 0.9.7.1**: Integração Swagger/OpenAPI para documentação interativa
- **pytest 9.0.1**: Framework de testes
- **pytest-flask 1.3.0**: Extensão do pytest para testes Flask
- **pytest-cov 7.0.0**: Plugin para cobertura de código
- **flask-cors 6.0.1**: Suporte a CORS
- **Docker**: Containerização da aplicação
- **Docker Compose**: Orquestração de containers

## Próximos Passos sugeridos

Possíveis melhorias e extensões futuras:

- Adicionar rate limiting para proteção contra abuso
- Implementar logging estruturado
- Adicionar métricas e monitoramento (Prometheus, Grafana)
- Suporte a múltiplos idiomas nas mensagens de erro
- Cache de validações frequentes
- Documentação adicional de arquitetura (diagramas)
