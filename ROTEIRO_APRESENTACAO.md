# Roteiro de Apresentação - Itaú Backend Challenge

## INTRODUÇÃO

Apresentar a solução: API RESTful em Python para validação de senhas. Explicar estrutura e decisões arquiteturais.

---

## PARTE 1: INFRAESTRUTURA

### Estrutura do Projeto
- Separação entre código fonte, testes e configuração

### Dependências (`requirements.txt`)
- Flask: framework leve para APIs RESTful
- Flasgger: documentação Swagger automática
- Pytest: testes

### Docker
- `Dockerfile`: imagem otimizada para produção
- `docker-compose.yml`: desenvolvimento local

### Aplicação (`app.py`)
- Factory Pattern com `create_app()`
- Blueprints para organização de rotas
- Error handlers centralizados

---

## PARTE 2: CAMADA DE DOMÍNIO

### Clean Architecture
- Lógica de negócio independente de frameworks
- Testável sem servidor HTTP
- Reutilizável em diferentes contextos

### Strategy Pattern (`password_validation_rule.py`)
- Interface abstrata para todas as regras
- Permite adicionar novas regras sem modificar código existente

### Regras de Validação (`rules/`)
- Cada regra implementa a interface
- Single Responsibility Principle
- Exemplos:
  - `minimum_length_rule.py`: tamanho mínimo configurável
  - `contains_digit_rule.py`: usa `any()` com generator
  - `contains_special_character_rule.py`: Set para lookup O(1)
  - `no_repeated_characters_rule.py`: Set para detectar duplicatas
  - `no_whitespace_rule.py` e `non_empty_password_rule.py`: separadas

### Serviço de Validação (`password_validator.py`)
- Orquestra todas as regras
- Dependency Injection via construtor
- Dois métodos:
  - `is_valid()`: retorna boolean (otimizado, short-circuit)
  - `validate()`: retorna violações detalhadas (melhor UX)

---

## PARTE 3: CAMADA DE API

### Separação de Camadas (`api/web/`)
- API apenas recebe HTTP e formata respostas
- Lógica de negócio no domínio

### Controllers (`password_controller.py`)
- Blueprint para organização
- Handler comum reutilizável
- Endpoints de exemplo dinâmicos

### Validação de Entrada (`request_validator.py`)
- Valida Content-Type, campos e tipos
- Fail-fast

### Tratamento de Erros (`error_handler.py`)
- Erros centralizados
- Respostas JSON padronizadas

### Swagger (`swagger_config.py`)
- Documentação interativa
- Exemplos e respostas documentadas

---

## PARTE 4: TESTES

### Estrutura
- Espelha estrutura de produção

### Testes Unitários (`tests/domain/validation/rules/`)
- Cada regra testada isoladamente
- Casos válidos, inválidos e edge cases

### Testes de Integração (`test_password_validator.py`)
- Serviço completo testado
- Todos os casos do enunciado

### Testes E2E (`test_password_controller.py`)
- Endpoints testados via cliente Flask
- Validação de códigos HTTP e formato de resposta

---

## PARTE 5: DECISÕES ARQUITETURAIS

### Clean Architecture
- Separação clara entre camadas
- Domínio independente de tecnologias

### SOLID
- Single Responsibility: cada classe uma responsabilidade
- Open/Closed: aberto para extensão, fechado para modificação
- Dependency Inversion: depende de abstrações

### Design Patterns
- Strategy Pattern: regras isoladas
- Factory Pattern: criação de aplicação
- Dependency Injection: regras via construtor

### Escalabilidade
- Stateless: múltiplas instâncias
- Early return otimizado
- Algoritmos eficientes (O(n) ou melhor)

---

## CONCLUSÃO

- Arquitetura sólida com Clean Architecture
- Testes completos
- Extensível (fácil adicionar regras)
- Escalável (stateless, horizontal scaling)
- Boas práticas (SOLID, Design Patterns)
