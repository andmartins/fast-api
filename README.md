# FastAPI - Configuração e Execução

## Introdução

Este repositório contém um projeto utilizando **FastAPI**, um framework web moderno e de alto desempenho para Python. Este guia explica os principais comandos para configurar, ativar e executar o ambiente de desenvolvimento.

---

## Configuração do Ambiente Virtual

Antes de iniciar o desenvolvimento, é recomendado criar um ambiente virtual para isolar as dependências do projeto.

### 1. Criar um ambiente virtual

```bash
python -m venv fastapi-env
```

### 2. Ativar o ambiente virtual

No **Windows (Git Bash ou WSL)**:

```bash
source fastapi-env/Scripts/activate
```

No **Windows (cmd)**:

```cmd
fastapi-env\Scripts\activate.bat
```

No **Mac/Linux**:

```bash
source fastapi-env/bin/activate
```

---

## Instalação do FastAPI

Com o ambiente virtual ativado, instale as dependências do FastAPI:

```bash
pip install "fastapi[standard]"
```

Essa instalação inclui o **Uvicorn**, um servidor ASGI recomendado para rodar a aplicação.

---

## Executando a API

Para iniciar o servidor de desenvolvimento:

```bash
fastapi dev main.py
```

O servidor iniciará na porta **8000** por padrão.

---

## Acessando a Documentação Interativa

FastAPI gera automaticamente documentação interativa para sua API.

- **Swagger UI (Documentação Padrão)**:
  [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)

- **Redoc (Documentação Alternativa)**:
  [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Finalização

Para desativar o ambiente virtual, execute:

```bash
deactivate
```

Agora seu projeto está pronto para desenvolvimento! 🚀
