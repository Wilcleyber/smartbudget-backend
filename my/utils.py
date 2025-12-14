from datetime import datetime, timedelta
from models.transaction_model import Transaction

def obter_data_atual():
    return datetime.now()

def calcular_saldo(transactions: list[Transaction]) -> float:
    saldo = sum(t.value for t in transactions)
    return saldo

def filtrar_por_periodo(transactions: list[Transaction], intervalo: str) -> list[Transaction]:
    agora = obter_data_atual()

    if intervalo == "30dias":
        limite = agora - timedelta(days=30)
        return [t for t in transactions if t.date >= limite]

    elif intervalo == "1ano":
        limite = agora - timedelta(days=365)
        return [t for t in transactions if t.date >= limite]

    elif intervalo == "total":
        return transactions
    else:
        return []
