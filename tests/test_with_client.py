import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from fastapi.testclient import TestClient
import main

client = TestClient(main.app)

print('Register alice:', client.post('/register', params={'username':'alice'}).json())
print('Create tx:', client.post('/transactions', params={'username':'alice'}, json={
    'name':'Teste', 'value':100.0, 'date':'2025-06-01', 'type':'entrada', 'category':'Teste', 'description':'desc'
}).json())
print('List txs:', client.get('/transactions', params={'username':'alice'}).json())
alltx = client.get('/transactions', params={'username':'alice'}).json()
if alltx:
    txid = alltx[0]['id']
    print('Update tx:', client.put(f'/transactions/{txid}', params={'username':'alice'}, json={
        'id': txid, 'name':'Teste','value':150.0,'date':'2025-06-01','type':'entrada','category':'Teste','description':'desc edit'
    }).json())
    print('List after update:', client.get('/transactions', params={'username':'alice'}).json())
else:
    print('No transactions to update')

print('Analytics summary:', client.get('/api/analytics/summary', params={'username':'alice'}).json())
print('Analytics monthly:', client.get('/api/analytics/monthly', params={'username':'alice'}).json())
