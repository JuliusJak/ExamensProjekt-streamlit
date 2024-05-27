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

