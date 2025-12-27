from models.transaction_model import Transaction
from uuid import uuid4
from datetime import datetime
import calendar
from models.user_model import users_data


def get_all_transactions(user: str):
    return users_data.get(user, [])


def add_transaction(user: str, data: Transaction):
    # usar cópia para evitar compartilhar a mesma instância entre listas
    new_tx = data.copy()
    if not new_tx.id:
        new_tx.id = str(uuid4())
    if user not in users_data:
        users_data[user] = []
    users_data[user].append(new_tx)


def update_transaction(user: str, id: str, data: Transaction):
    if user not in users_data:
        return False
    for idx, t in enumerate(users_data[user]):
        if t.id == id:
            # preservar o id e substituir os campos usando cópia
            updated = data.copy()
            updated.id = id
            users_data[user][idx] = updated
            return True
    return False


def delete_transaction(user: str, id: str):
    if user not in users_data:
        return False

    original_length = len(users_data[user])
    users_data[user] = [t for t in users_data[user] if t.id != id]

    return len(users_data[user]) < original_length

def load_demo_data():
    # gerar datas dinâmicas a partir do mês atual
    now = datetime.now()
    # templates com offset de meses e dias desejados
    demo_templates = [
        ( -5, 1, "Salário", 3000, "entrada", "Trabalho", "Salário mensal" ),
        ( -4, 15, "Freelance", 800, "entrada", "Trabalho", "Projeto extra" ),
        ( -4, 10, "Supermercado", 450, "saida", "Alimentação", "Compras do mês" ),
        ( -3, 12, "Transporte", 200, "saida", "Transporte", "Combustível e ônibus" ),
        ( -2, 20, "Cinema", 80, "saida", "Lazer", "Filme com amigos" ),
        ( -5, 5, "Plano de saúde", 300, "saida", "Saúde", "Mensalidade" ),
    ]

    transactions = []
    for offset_months, day, name, value, ttype, category, desc in demo_templates:
        # calcular ano/mês com offset
        month = now.month + offset_months
        year = now.year + (month - 1) // 12
        month = ((month - 1) % 12) + 1
        # ajustar dia para o último dia do mês quando necessário
        last_day = calendar.monthrange(year, month)[1]
        d = min(day, last_day)
        date_str = f"{year:04d}-{month:02d}-{d:02d}"
        transactions.append(Transaction(
            id=str(uuid4()),
            name=name,
            value=value,
            date=date_str,
            type=ttype,
            category=category,
            description=desc
        ))
    return transactions





