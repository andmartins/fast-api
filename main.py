"""
Este módulo contém uma API simples usando FastAPI.

Endpoints disponíveis:
- `/` : Retorna uma mensagem de boas-vindas.
- `/items/{item_id}` : Retorna um item baseado no ID informado.
"""

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Retorna uma mensagem de boas-vindas."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """Retorna uma mensagem de boas-vindas."""
    return {"item_id": item_id, "q": q}
