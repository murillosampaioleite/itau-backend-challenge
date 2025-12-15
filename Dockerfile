FROM python:3.14-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Desabilitar criação de __pycache__
ENV PYTHONDONTWRITEBYTECODE=1

# Copiar arquivos de dependências
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Expor porta
EXPOSE 8080

# Comando para executar a aplicação
CMD ["python", "app.py"]
