import requests
import json

data = {
    'user_name': 'Shivam',
    'age': 24,
    'city': 'Delhi',
}

json_data = json.dumps(data)
response = requests.post(url='http://127.0.0.1:8000/create_user', data=json_data)
user_data = response.json()
print(user_data)