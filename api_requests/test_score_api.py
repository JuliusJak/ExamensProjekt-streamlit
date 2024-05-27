import requests


def add_test_score(test_score):

    url = "http://localhost:8082/test/add"

    response = requests.post(url, json=test_score)

    print(response.status_code)
    print(response.json())


# test_score = {
#     "username": "bob",
#     "testType": "regular_test",
#     "amountOfTestQuestions": 9,
#     "correctAnswers": 9
# }
# add_test_score(test_score)

def get_users_test_scores(username):
    
    url = "http://localhost:8082/test/testScores"

    params = {
        "username": username
    }
    
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 204:
        print(f"No content found. Status code {response.status_code}")
    else:
        print(f"Request failed with status code {response.status_code}")
