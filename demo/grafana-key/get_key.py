import requests
import time


headers = {
    'Content-Type': 'application/json',
}

data = '{"name":"api32", "role": "Admin"}'

time.sleep(10)
response = requests.post('http://admin:admin@grafana:3000/api/auth/keys', headers=headers, data=data)

try:
    key = response.json()['key']
    with open('/grafana-key/key.txt', 'w') as out:
        out.write(key)
except KeyError:
    pass


