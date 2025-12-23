from models.transaction_model import Transaction
from uuid import uuid4
from datetime import datetime
import json
import os

users_data = {}

def get_all_transactions(user: str):
    return users_data.get(user, [])

def add_transaction(user: str, data: Transaction):
    data.id = str(uuid4())
    if user not in users_data:
        users_data[user] = []
    users_data[user].append(data)

def delete_transaction(user: str, id: UUID):
    if user not in users_data:
        return False
    
    original_length = len(users_data[user])
    users_data[user] = [t for t in users_data[user] if t.id != id]

    return len(users_data[user]) < original_length

def load_demo_data():
    demo = [
        {
            "name": "Salário",
            "value": 3000,
            "date": "2025-06-01",
            "type": "entrada",
            "category": "Trabalho",
            "description": "Salário mensal"
        },
        {
            "name": "Freelance",
            "value": 800,
            "date": "2025-06-15",
            "type": "entrada",
            "category": "Trabalho",
            "description": "Projeto extra"
        },
        {
            "name": "Supermercado",
            "value": 450,
            "date": "2025-06-10",
            "type": "saida",
            "category": "Alimentação",
            "description": "Compras do mês"
        },
        {
            "name": "Transporte",
            "value": 200,
            "date": "2025-06-12",
            "type": "saida",
            "category": "Transporte",
            "description": "Combustível e ônibus"
        },
        {
            "name": "Cinema",
            "value": 80,
            "date": "2025-06-20",
            "type": "saida",
            "category": "Lazer",
            "description": "Filme com amigos"
        },
        {
            "name": "Plano de saúde",
            "value": 300,
            "date": "2025-06-05",
            "type": "saida",
            "category": "Saúde",
            "description": "Mensalidade"
        }
    ]
    transactions = []
    for item in demo:
        transactions.append(Transaction(
            id=str(uuid4()),              # converter UUID para string
            name=item["name"],
            value=item["value"],
            date=item["date"],            # já como string
            type=item["type"],
            category=item["category"],    # garantir que existe
            description=item["description"] # garantir que existe
        ))
    return transactions





