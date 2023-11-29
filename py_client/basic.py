import requests

# GET method endpoint
# endpoint = "http://localhost:8000/api/"   # "http://127.0.0.1:8000/"

# POST method endpoint
endpoint = "http://localhost:8000/api/post/"   # "http://127.0.0.1:8000/"


# GET method request
# get_response = requests.get(endpoint, params={'abc': 123}, json={"query": "Hey there!"})

# POST method request
get_response = requests.post(endpoint, json={"title": "Washing Machine1", "content": "This is a washing machine", "price": 20000.23, "my_discount": 180})
# print(get_response.status_code)
# print(get_response.text)
print(get_response.json())