import requests

def save_image_question(image_question):

    url = "http://localhost:8082/image-questions"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, json=image_question, headers=headers)

    if response.status_code == 201:
        print("ImageQuestion saved successfully.")
    else:
        print(f"Failed to save ImageQuestion. Status code: {response.status_code}")
        print(f"Response: {response.json()}")

    return response


def get_image_questions(id=None, name=None, question=None):
    
    url = "http://localhost:8082/image-questions/search"
    params = {
        'id': id,
        'name': name,
        'question': question
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("ImageQuestions retrieved successfully.")
        print(response.json())
    elif response.status_code == 404:
        print("No ImageQuestions found.")
    else:
        print(f"Failed to retrieve ImageQuestions. Status code: {response.status_code}")
        print(f"Response: {response.json()}")

    return response.json()

