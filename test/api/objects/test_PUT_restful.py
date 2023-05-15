import pytest
import requests
import json
from constants import BASE_URL, DEFAULT_PAYLOAD, headers, request_url

def POST_create_new_data(payload=DEFAULT_PAYLOAD):
    response = requests.post(request_url, data=json.dumps(payload), headers=headers)
    created_object = response.json()
    return created_object

def test_put_update_existing_object_name():
    created_object_id = POST_create_new_data()["id"]
    created_object_endpoint = f"{request_url}/{created_object_id}"

    put_payload = {"name": "Apple AirPods", "data": {"color": "white", "generation": "3rd", "price": 120}}
    put_response = requests.put(created_object_endpoint, data=json.dumps(put_payload), headers=headers)
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
    put_response = requests.put(put_endpoint, data=json.dumps(put_payload), headers=headers)
    print(f"PUT content: {put_response.content}")
    assert put_response.status_code == 404

# The follow tests fail because REST API accepts PUT requests that are malformed, if this is acceptable the assertions could be changed or the tests removed

def test_put_invalid_data_type():
    created_object_id = POST_create_new_data()["id"]
    created_object_endpoint = f"{request_url}/{created_object_id}"

    put_payload = {"name": "Test Product", "data": {"color": "blue", "price": "invalid"}}
    put_response = requests.put(created_object_endpoint, data=json.dumps(put_payload), headers=headers)
    assert put_response.status_code == 400

def test_put_extra_field():
    created_object_id = POST_create_new_data()["id"]
    created_object_endpoint = f"{request_url}/{created_object_id}"

    put_payload = {"name": "Test Product", "extra_field": "Not required", "data": {"color": "blue", "price": 99}}
    put_response = requests.put(created_object_endpoint, data=json.dumps(put_payload), headers=headers)
    assert put_response.status_code == 400

def test_put_empty_json():
    created_object_id = POST_create_new_data()["id"]
    created_object_endpoint = f"{request_url}/{created_object_id}"

    put_response = requests.post(created_object_endpoint, json={}, headers=headers)
    assert put_response.status_code == 400