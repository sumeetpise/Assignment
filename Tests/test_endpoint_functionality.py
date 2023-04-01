import requests

#Add/Create a new user by using post request
def test_create_request(api_url, json_data):
    response = requests.post(api_url + '/api/users',json=json_data)
    print(response)
    print(response.json())
    assert response.json()['job']=='automation'
    assert response.status_code == 201


#update an existing user by using put request
def test_update_request(api_url, json_data):
    response = requests.put(api_url + '/api/users/2',json=json_data)
    print(response)
    print(response.json())
    assert response.json()['job']=='automation'
    assert response.status_code == 200

#delete an existing user by using delete request
def test_delete_request(api_url, json_data):
    response = requests.delete(api_url + '/api/users/2',json=json_data)
    print(response)
    assert response.status_code == 204


