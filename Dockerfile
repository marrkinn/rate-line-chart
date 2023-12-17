# Use uma imagem base do Python
FROM python:3.8

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Criar e definir o diretório de trabalho
WORKDIR /app

# Copiar os requisitos do projeto para o contêiner
COPY requirements.txt /app/

# Instalar as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o restante do aplicativo para o contêiner
# COPY . /app/