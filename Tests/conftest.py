import pytest

#fixture to return the base url
@pytest.fixture
def api_url():
    return "https://reqres.in"

#fixture to return the data to validate endpoint functionality for CRUD
@pytest.fixture
def json_data():
    return {
    "name": "Sumeet",
    "job": "automation"
}