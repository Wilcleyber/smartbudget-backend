from fastapi import APIRouter, HTTPException
from typing import List

from models.user_model import active_users
from models.transaction_model import Transaction
from crud.transactions import (
    get_all_transactions,
    add_transaction,
    delete_transaction,
    users_data,
    load_demo_data
)

router = APIRouter()

@router.post("/login")
def login(username: str):
    if username == "visitante":
        return {"message": "Usuário visitante logado com sucesso."}
    if username not in users_data:
        raise HTTPException(status_code=404, detail="Usuário não registrado.")
    if username not in active_users:
        active_users.append(username)
    return {"message": f"Usuário {username} logado com sucesso."}

@router.post("/register")
def register(username: str):
    if username in active_users:
        raise HTTPException(status_code=400, detail="Usuário já registrado.")
    active_users.append(username)
    users_data[username] = []
    return {"message": f"Usuário {username} registrado com sucesso."}

@router.get("/transactions", response_model=List[Transaction])
def get_transactions(username: str):
    if username == "visitante":
        return load_demo_data()
    if username not in users_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return get_all_transactions(username)

@router.post("/transactions")
def post_transaction(username: str, transaction: Transaction):
    if username not in users_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    add_transaction(username, transaction)
    return {"message": "Transação adicionada com sucesso."}

@router.delete("/transactions/{id}")
def delete_transaction_by_id(id: str, username: str):
    if username not in users_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    success = delete_transaction(username, id)
    if not success:
        raise HTTPException(status_code=404, detail="Transação não encontrada.")
    return {"message": "Transação removida com sucesso."}
