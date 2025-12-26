from pydantic import BaseModel
from typing import Optional

class Transaction(BaseModel):
    id: Optional[str] = None
    name: str
    value: float
    date: str   # formato "YYYY-MM-DD"
    type: str   # "entrada" ou "saida"
    category: str
    description: str
