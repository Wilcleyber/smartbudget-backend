from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    id: str
    name: str
    value: float
    date: str   # formato "YYYY-MM-DD"
    type: str   # "entrada" ou "saida"
    category: str
    description: str
