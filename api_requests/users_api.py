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

def get_user(username:str|None, password:str|None, role:str|None, id:int|None) -> dict|None:
    """Searches for users in the DB matching the given parameters

    Parameters
    ----------
    username
        Users username
    password
        Users password
    role
        Users role
    id
        Users account id

    Returns
    -------
        The user that matches the search
    """

    url = "http://localhost:8082/users/search"

    params = {
        "username": username,
        "password": password,
        "id":id,
        "role":role
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")

def update_user(user_id:int, new_username:str|None=None, new_password:str|None=None, new_role:str|None=None) -> str:
    """Select a user by their Id and then update their information by inputting new parameters

    Parameters
    ----------
    user_id
        This is how the script knows what user to update
    new_username, optional
        A string that will become the new username, by default None
    new_password, optional
        A string that will become the new password, by default None
    new_role, optional
        A string that will become the new role, by default None

    Returns
    -------
        A string saying the user have been successfully updated
    """

    url = "http://localhost:8082/users/update"

    params = {
        "newUsername": new_username,
        "newPassword": new_password,
        "id":user_id,
        "newRole":new_role
    }

    response = requests.put(url, params=params)

    if response.status_code == 200:
        return response.content
    else:
        return f"Request failed with status code {response.status_code}"


def delete_user(user_id:int) -> str:

    url = "http://localhost:8082/users/delete"

    params = {
        "id":user_id
    }

    response = requests.delete(url,params=params)

    if response.status_code == 200:
        return response.content
    else:
        return f"Request failed with status code {response.status_code}"
    
