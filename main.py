"""
Este módulo contém uma API simples usando FastAPI.

Endpoints disponíveis:
- `/` : Retorna uma mensagem de boas-vindas.
- `/items/{item_id}` : Retorna um item baseado no ID informado.
"""

from typing import Optional, Dict, Any
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(
    item_id: int,
    q: Optional[str] = None
) -> Dict[str, Any]:
    """Retorna um item baseado no ID informado."""
    return {
        "item_id": item_id,
        "q": q
    }
