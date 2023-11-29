import requests


# work only if have a user's token
# headers = {'Authorization': 'Bearer b8618824d7754f9e12abeaed9a9520d7a42ca707'}

endpoint = "http://localhost:8000/api/products/" 

data = {
    "title": "This field is being created again",
    "price": 3433.33
}

# get_response = requests.post(endpoint, json=data, headers=headers)
get_response = requests.post(endpoint, json=data)

print(get_response.json())