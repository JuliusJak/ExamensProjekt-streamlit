import requests

def create_new_user(username:str, password:str, role:str|None=None) -> dict|set:
    """Creates a new user using the backend api

    Parameters
    ----------
    username
        A string for the new users username
    password
        A string for the new users password
    role
        A string for the new users role

    Returns
    -------
        If successfull returns a copy of the user else it will return the error message
    """

    url = "http://localhost:8082/users/create"

    user_data = {
        "username": username,
        "password": password,
        "role": role
    }

    response = requests.post(url, json=user_data)

    if response.status_code == 201:
        return response.json()
    
    elif response.status_code == 409:
        return "Username already exists. Please choose a different username."

    else:
        return f"Failed to create user. Status code: {response.status_code}, Message: {response.text}"

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
