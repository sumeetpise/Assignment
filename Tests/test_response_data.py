import requests

#Checks if for the response data is in valid json format
def test_response_data(api_url):
    response = requests.get(api_url + '/api/users')
    assert response.headers["Content-Type"]
    print(response)
    print(response.json())
    assert response.json()