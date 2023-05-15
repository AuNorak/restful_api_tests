import pytest
import requests
from constants import BASE_URL, DEFAULT_PAYLOAD, headers, request_url

def test_post_valid_data():
    response = requests.post(request_url, json=DEFAULT_PAYLOAD, headers=headers)
    assert response.status_code == 201
    created_object = response.json()
    assert created_object["name"] == DEFAULT_PAYLOAD["name"]
    assert created_object["data"]["color"] == DEFAULT_PAYLOAD["data"]["color"]
    assert created_object["data"]["price"] == DEFAULT_PAYLOAD["data"]["price"]

def test_post_invalid_json():
    invalid_json = '{"name": "Test Product", "data": {"color": "blue", "price": 99}'
    response = requests.post(request_url, json=invalid_json, headers=headers)
    assert response.status_code == 400

    # The follow tests fail because REST API accepts POST requests that are malformed, if this is acceptable the assertions could be changed or the tests removed

def test_post_missing_required_field():
    new_object = {"data": {"color": "blue", "price": 99}}
    response = requests.post(request_url, json=new_object, headers=headers)
    assert response.status_code == 400

def test_post_invalid_data_type():
    new_object = {"name": "Test Product", "data": {"color": "blue", "price": "invalid"}}
    response = requests.post(request_url, json=new_object, headers=headers)
    assert response.status_code == 400

def test_post_extra_field():
    new_object = {"name": "Test Product", "extra_field": "Not required", "data": {"color": "blue", "price": 99}}
    response = requests.post(request_url, json=new_object, headers=headers)
    assert response.status_code == 400

def test_post_empty_json():
    response = requests.post(request_url, json={}, headers=headers)
    assert response.status_code == 400