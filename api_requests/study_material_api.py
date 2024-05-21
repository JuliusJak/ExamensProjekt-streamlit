import requests

def get_all_study_material() -> dict:
    """Fetches all the study material from the DB

    Returns
    -------
        all the study material as json
    """
    url = "http://localhost:8082/study/study-materials"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")

def study_material_search(query:str):

    url = "http://localhost:8082/study/study-materials/search"

    params = {
        "content": query
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code {response.status_code}")
