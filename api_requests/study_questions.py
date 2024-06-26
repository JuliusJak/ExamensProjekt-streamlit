import requests

def get_questions() -> dict|str:

    url = "http://localhost:8082/questions/get"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    else:
        return f"Failed to fetch questions. Status code: {response.status_code}, Message: {response.text}"
    
def create_question(question_body:dict) -> dict|str:
    
    url = "http://localhost:8082/questions/create"

    response = requests.post(url,json=question_body)

    if response.status_code == 201:
        return response.json()
    else:
        return f"Failed to create question. Status code: {response.status_code}, Message: {response.text}"

def delete_question(user_id:int) -> str:

    url = "http://localhost:8082/questions/delete"

    params = {
        "id":user_id
    }

    response = requests.delete(url,params=params)

    if response.status_code == 200:
        return response.content
    else:
        return f"Request failed with status code {response.status_code}"
    
def get_random_questions(category_id:str|None=None) -> dict|str:

    url = "http://localhost:8082/questions/random"

    params = {
        "categoryId": category_id
    }
    response = requests.get(url,params=params)

    if response.status_code == 200:
        return response.json()
    
    else:
        return f"Failed to fetch questions. Status code: {response.status_code}, Message: {response.text}"
    