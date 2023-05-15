import pytest
import requests
from constants import request_url

def test_delete_existing_object(objects_fixture):
    created_object_endpoint = f"{request_url}/{objects_fixture}"

    response = requests.delete(created_object_endpoint)
    assert response.status_code == 200
    response = requests.get(created_object_endpoint)
    assert response.status_code == 404

def test_delete_non_existing_object():
    non_existing_object_endpoint = f"{request_url}/999999" 
    response = requests.delete(non_existing_object_endpoint)
    assert response.status_code == 404
 
    # Delete an object in use; do we allow deleting an object in use?

    # Concurrent deletion