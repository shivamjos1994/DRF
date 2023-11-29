import requests


endpoint = "http://localhost:8000/api/products/2/update/" 

data = {
    "title": "New Fridge to check UpdateModelMixin1",
    "price": 320023.23
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())