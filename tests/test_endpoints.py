import requests, time
base = 'http://127.0.0.1:8000'

def show(resp):
    try:
        return resp.status_code, resp.json()
    except Exception:
        return resp.status_code, resp.text

# wait for server
for _ in range(20):
    try:
        requests.get(base + '/')
        break
    except Exception:
        time.sleep(0.5)

print('Register alice:', show(requests.post(base + '/register', params={'username':'alice'})))
print('Create tx:', show(requests.post(base + '/transactions', params={'username':'alice'}, json={
    'name':'Teste', 'value':100.0, 'date':'2025-06-01', 'type':'entrada', 'category':'Teste', 'description':'desc'
})))
print('List txs:', show(requests.get(base + '/transactions', params={'username':'alice'})))
alltx = requests.get(base + '/transactions', params={'username':'alice'}).json()
if alltx:
    txid = alltx[0]['id']
    print('Update tx:', show(requests.put(base + f'/transactions/{txid}', params={'username':'alice'}, json={
        'id': txid, 'name':'Teste','value':150.0,'date':'2025-06-01','type':'entrada','category':'Teste','description':'desc edit'
    })))
    print('List after update:', show(requests.get(base + '/transactions', params={'username':'alice'})))
else:
    print('No transactions to update')

print('Analytics summary:', show(requests.get(base + '/api/analytics/summary', params={'username':'alice'})))
print('Analytics monthly:', show(requests.get(base + '/api/analytics/monthly', params={'username':'alice'})))
