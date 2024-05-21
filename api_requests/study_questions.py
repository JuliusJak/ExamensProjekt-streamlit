import requests

def get_questions():

    url = "http://localhost:8082/test/questions"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    else:
        return f"Failed to create user. Status code: {response.status_code}, Message: {response.text}"
    
