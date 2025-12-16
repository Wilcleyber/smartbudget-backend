from fastapi import APIRouter, HTTPException
from models.transaction_model import Transaction
from models.user_model import users_data
from datetime import datetime
from collections import defaultdict

router = APIRouter(prefix="/api/analytics", tags=["Analytics"])

@router.get("/summary")
def get_summary(username: str):
    if username not in users_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    transactions = users_data[username]
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
    if username not in users_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    transactions = users_data[username]
    categorias = defaultdict(float)
    for t in transactions:
        categorias[t.category] += t.value
    return categorias

@router.get("/monthly")
def get_monthly(username: str):
    if username not in users_data:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    transactions = users_data[username]
    meses = defaultdict(lambda: {"receitas": 0, "despesas": 0})
    for t in transactions:
        mes = datetime.strptime(t.date, "%Y-%m-%d").strftime("%Y-%m")
        if t.type == "entrada":
            meses[mes]["receitas"] += t.value
        else:
            meses[mes]["despesas"] += t.value
    return meses