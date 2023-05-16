import pytest
import requests
from constants import headers, request_url

def test_put_update_existing_object_name(objects_fixture):
    created_object_endpoint = f"{request_url}/{objects_fixture}"

    put_payload = {"name": "Apple AirPods", "data": {"color": "white", "generation": "3rd", "price": 120}}
    put_response = requests.put(created_object_endpoint, json=put_payload, headers=headers)
    assert put_response.status_code == 200
    print(f"PUT content: {put_response.content}")

    get_response = requests.get(created_object_endpoint, headers=headers)
    assert get_response.status_code == 200
    fetched_object = get_response.json()
    assert fetched_object["data"]["price"] == 120

def test_put_update_non_existent_object():
    non_existent_id = 9999
    put_endpoint = f"{request_url}/{non_existent_id}"

    put_payload = {"name": "Apple AirPods", "data": {"color": "white", "generation": "3rd", "price": 120}}
    put_response = requests.put(put_endpoint, json=put_payload, headers=headers)
    print(f"PUT content: {put_response.content}")
    assert put_response.status_code == 404

# The following tests fail because REST API accepts PUT requests that are malformed, if this is acceptable the assertions could be changed or the tests removed
def test_put_invalid_data_type(objects_fixture):
    created_object_endpoint = f"{request_url}/{objects_fixture}"

    put_payload = {"name": "Test Product", "data": {"color": "blue", "price": "invalid"}}
    put_response = requests.put(created_object_endpoint, json=put_payload, headers=headers)
    assert put_response.status_code == 400

def test_put_extra_field(objects_fixture):
    created_object_endpoint = f"{request_url}/{objects_fixture}"

    put_payload = {"name": "Test Product", "extra_field": "Not required", "data": {"color": "blue", "price": 99}}
    put_response = requests.put(created_object_endpoint, json=put_payload, headers=headers)
    assert put_response.status_code == 400

# The following test fails because REST API returns 405, which is not the correct error code
def test_put_empty_json(objects_fixture):
    created_object_endpoint = f"{request_url}/{objects_fixture}"

    put_response = requests.post(created_object_endpoint, json={}, headers=headers)
    assert put_response.status_code == 400