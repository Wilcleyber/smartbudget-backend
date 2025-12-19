from fastapi import APIRouter, HTTPException
from models.transaction_model import Transaction
from models.user_model import users_data
from crud.transactions import load_demo_data
from datetime import datetime
from collections import defaultdict


router = APIRouter(prefix="/api/analytics", tags=["Analytics"])

def get_transactions_for_user(username: str):
    if username == "visitante":
        return load_demo_data()
    elif username in users_data:
        return users_data[username]
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")

@router.get("/summary")
def get_summary(username: str):
    transactions = get_transactions_for_user(username)
    total_receitas = sum(t.value for t in transactions if t.type == "entrada")
    total_despesas = sum(t.value for t in transactions if t.type == "saida")
    saldo = total_receitas - total_despesas
    return {
        "total_receitas": total_receitas,
        "total_despesas": total_despesas,
        "saldo_atual": saldo
    }

@router.get("/by-category")
def get_by_category(username: str):
    transactions = get_transactions_for_user(username)
    categorias = defaultdict(float)
    for t in transactions:
        categorias[t.category] += t.value
    return categorias

@router.get("/monthly")
def get_monthly(username: str):
    transactions = get_transactions_for_user(username)
    meses = defaultdict(lambda: {"receitas": 0, "despesas": 0})
    for t in transactions:
        # garantir que a data está no formato YYYY-MM-DD
        mes = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
        if t.type == "entrada":
            meses[mes]["receitas"] += t.value
        else:
            meses[mes]["despesas"] += t.value
    return meses