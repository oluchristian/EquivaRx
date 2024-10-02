import requests

link = "http://127.0.0.1:5000/api/v1/upload/"
response = requests.post(link)
if response.headers.get('Content-Type') == 'application/json':
    print(response.json())
else:
    print(response.text)
    