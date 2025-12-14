from models.transaction_model import Transaction
from uuid import uuid4, UUID
from datetime import datetime
import json
import os

users_data = {}

def get_all_transactions(user: str):
    return users_data.get(user, [])

def add_transaction(user: str, data: Transaction):
    data.id = uuid4()
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

    file_path = os.path.join("data", "demodata.json")
    with open(file_path, "r", encoding="utf-8") as f:
        demo_data = json.load(f)

    transactions = []
    for item in demo_data:
        transactions.append(
            Transaction(
                id=uuid4(),  # Gera novo UUID para cada transação
                name=item["name"],
                value=item["value"],
                date=datetime.fromisoformat(item["date"]),
                type=item["type"]
            )
        )
    return transactions





