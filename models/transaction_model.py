from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class Transaction(BaseModel):
    id: UUID
    name: str 
    value: float  
    date: datetime  
    type: str   
