import pytest
import requests
import json

BASE_URL = "https://api.restful-api.dev"




@pytest.fixture
def existing_object():
    object_id = 6
    response = requests.get(f"{BASE_URL}/objects/{object_id}")
    return response.json()

@pytest.fixture
def existing_object_endpoint(existing_object):
    return f"{BASE_URL}/objects/{existing_object['id']}"

def test_update_existing_object_name(existing_object, existing_object_endpoint):
    headers = {"content-type": "application/json"}
    payload = json.dumps({ "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
    requestUrl = "https://api.restful-api.dev/objects/6"
    r = requests.put(requestUrl, data=payload, headers=headers)
    response = requests.get(existing_object_endpoint)
    fetched_object = response.json()
    assert fetched_object['data']['price'] == 135

# def test_update_existing_object_name(existing_object, existing_object_endpoint):
#     headers = {"content-type": "application/json"}
#     updated_object = {'name': f"updated_{existing_object['name']}"}
#     response = requests.put(existing_object_endpoint, json=updated_object, headers=headers)
#     assert response.status_code == 200

#     response = requests.get(existing_object_endpoint)
#     fetched_object = response.json()
    
#     assert fetched_object['name'] == updated_object['name']

# def test_update_non_existent_object(self):
#     non_existent_id = 9999
#     updated_object = {"key1": "updated_value1", "key2": "updated_value2"}
#     response = requests.put(f"{self.BASE_URL}/objects/{non_existent_id}", json=updated_object)

#     assert response.status_code == 404
