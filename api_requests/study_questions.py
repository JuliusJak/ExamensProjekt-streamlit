import requests

def get_questions():

    url = "http://localhost:8082/test/questions"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    else:
        return f"Failed to fetch questions. Status code: {response.status_code}, Message: {response.text}"
    
def create_question(question_body):
    
    url = "http://localhost:8082/test/questions/create"

    response = requests.post(url,json=question_body)

    if response.status_code == 201:
        return response.json()
    else:
        return f"Failed to create question. Status code: {response.status_code}, Message: {response.text}"
