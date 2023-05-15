import pytest
import requests
from constants import DEFAULT_PAYLOAD, headers, request_url

@pytest.fixture
def objects_fixture():
    payload = DEFAULT_PAYLOAD
    response = requests.post(request_url, json=payload, headers=headers)
    object_id = response.json()['id']
    yield object_id

    requests.delete(f"{request_url}/{object_id}")