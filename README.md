# Smartbudget Backend

Backend desenvolvido em FastAPI para controle de transações financeiras.
- Endpoints: login, register, transactions (GET, POST, DELETE)
- Modo visitante com dados simulados (`demodata.json`)
- Persistência em memória durante sessão

## Rodar localmente
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install fastapi uvicorn
python -m uvicorn main:app --reload