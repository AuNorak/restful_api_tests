import pytest
import requests
from constants import BASE_URL, DEFAULT_PAYLOAD, headers, request_url

@pytest.fixture
def objects_fixture():
    payload = DEFAULT_PAYLOAD
    response = requests.post(request_url, json=payload, headers=headers)
    object_id = response.json()['id']
    yield object_id

    requests.delete(f"{BASE_URL}/objects/{object_id}")