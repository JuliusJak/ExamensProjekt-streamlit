import requests

def get_user(username, password):
    url = "http://localhost:8082/users/search"

    params = {
        "username": username,
        "password": password
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
