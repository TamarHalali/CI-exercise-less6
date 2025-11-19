# test_flask_app.py
import requests
import sys

def test_add_item():
	url = "http://app:5000/add" 
	data = {"title": "Buy groceries"}

    try:
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

if _name_ == "_main_":
    test_add_item()
