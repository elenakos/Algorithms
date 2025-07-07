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

