import requests

url = "http://app:5000/add"
data = {
    "title": "Buy groceries"
}

response = requests.post(url, data=data)
