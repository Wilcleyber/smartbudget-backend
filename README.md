# SmartBudget Backend

Backend desenvolvido em FastAPI para controle de transações financeiras.

## Funcionalidades
- Autenticação de usuários
- CRUD de transações
- Modo visitante com dados simulados (`demodata.json`)
- **Novo módulo de análise de dados**:
  - Resumo geral (receitas, despesas, saldo)
  - Gastos por categoria
  - Evolução mensal
  - Top categorias mais gastas

## Rodar localmente
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
acesse: http://127.0.0.1:8000/docs

## Teste Online
https://smartbudget-backend-zgek.onrender.com\docs