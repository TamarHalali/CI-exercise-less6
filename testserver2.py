import time
import requests

url = "http://app:5000/add"
data = {"x":1}

for i in range(10):
    try:
        response = requests.post(url, data=data)
        print(response.text)
        break
    except requests.exceptions.ConnectionError:
        print("Server not ready, waiting 2 seconds...")
        time.sleep(2)

