import requests

#Checks for the response time
def test_response_time_status_code(api_url):
    response = requests.get(api_url)
    print(response)
    assert response.elapsed.total_seconds() < 1.0

