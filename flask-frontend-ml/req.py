import requests

url = 'http://127.0.0.1:5000/api'

data = {'value':1.8}
r = requests.post(url,json = data)

print(r.json())