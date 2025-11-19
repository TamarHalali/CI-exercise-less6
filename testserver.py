# test_flask_app.py
import requests
import sys
import time

def test_add_item():
    url = "http://app:5000/add"
    data = {"title": "Buy groceries"}

    try:
	time.sleep(10)
        response = requests.post(url, data=data)
    except Exception as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    if response.status_code in [200, 201]:
        print(f"Success! Status code: {response.status_code}")
        sys.exit(0)
    else:
        print(f"Failed! Status code: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    test_add_item()

