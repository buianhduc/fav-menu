# use to request server build in 1.py

import requests

url = 'http://127.0.0.1:5000/login';


response = requests.get(url)

print(response.status_code)
print(response.text)
# print(response.json())