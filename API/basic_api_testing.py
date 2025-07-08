'''
This is an example of using python/request to test API

To run/execute:
   Open a terminal and execute this command:
   % pytest basic_api_testing.py -s

'''

import requests

# VARIABLES
URL = "https://jsonplaceholder.typicode.com"

def test_get_response():
    print("\n*** TC: Verify GET returns 100 records")
    url = URL + "/posts"

    # Make the GET request
    response = requests.get(url)

    # Check the response
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print(f"Number of records: {len(response.json())}")
    assert response.json().__len__() == 100

def test_post_request():
    print("\n*** TC: Verify POST returns correct sent data")
    title = "Hello from Python"
    body = "Hello from Python"
    url = URL + "/posts"
    payload = {"title": title, "body": body}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    # Check the response
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    print(f"Saved data: {response.json()}")
    assert response.json().get("title") == title

