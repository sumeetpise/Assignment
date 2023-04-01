import requests

#hitting a valid URL
def test_success_status_code(api_url):
    response = requests.get(api_url)
    print(response)
    assert response.status_code == 200


#hitting an invalid URL
def test_notfound_status_code(api_url):
    response = requests.get(api_url + "/users")
    print(response)
    assert response.status_code == 404


#here im failing the test case to get assertion error
def test_unauthorized_status_code(api_url):
    response = requests.get(api_url + "/users")
    print(response)
    assert response.status_code == 401

