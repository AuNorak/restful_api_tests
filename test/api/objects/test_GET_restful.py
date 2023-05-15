import requests
from constants import request_url

class TestRestfulAPI():
    def test_get_all_objects_returns_200(self):
        response = requests.get(request_url)
        assert response.status_code == 200

    # def test_get_all_objects_as_unauthenticated_returns_403(self):
    #     endpoint = f"{request_url}/42"
    #     response = requests.get(endpoint)
    #     self.assertEqual(response.status_code, 403)
    # tests the endpoint returns 403 for a user without permission making get request

    def test_get_single_object_returns_200(self):
        endpoint = f"{request_url}/1"
        response = requests.get(endpoint)
        assert response.status_code == 200

    def test_get_multiple_object_returns_requested_objects(self):
        endpoint = f"{request_url}?id=1&id=4&id=5"
        response = requests.get(endpoint)
        data = response.json()
        expected_ids = ["1", "4", "5"]
        actual_ids = [obj['id'] for obj in data]
        assert actual_ids == expected_ids

    def test_get_multiple_same_object_returns_multiple_objects(self):
        endpoint = f"{request_url}?id=1&id=1&id=1"
        response = requests.get(endpoint)
        data = response.json()
        expected_ids = ["1","1","1"]
        actual_ids = [obj['id'] for obj in data]
        assert actual_ids == expected_ids
    # tests the endpoint returns the same object multiple times when queried for the same object multiple times, I wasn't sure what the behaviour would be here and 
    # was looking for a breaking case, there may be an argument to remove this

    def test_get_all_objects_returns_list_of_objects(self):
        response = requests.get(request_url)
        data = response.json()
        assert isinstance(data, list)
        for obj in data:
            assert isinstance(obj, dict)

    def test_get_single_object_shape(self):
        endpoint = f"{request_url}/1"
        response = requests.get(endpoint)
        data = response.json()
        expected_keys = ['id', 'name', 'data']
        assert set(data.keys()) == expected_keys
        assert isinstance(data.id, int)
        assert isinstance(data.name, str)
        assert isinstance(data.data, dict)

    def test_get_string_object_returns_404_with_error_payload(self):
        endpoint = f"{request_url}/jon"
        response = requests.get(endpoint)
        payload = {'error': 'Object with id=jon was not found.'}
        assert response.status_code == 404
        assert payload == response.json()
    # tests the endpoint returns 404 for a string object
    # there may be an argument to split out a seperate test for testing response payload
    # test fails, but this is a bug in restful API so I'm leaving the assertion as is

    def test_get_non_existent_object_returns_404(self):
        endpoint = f"{request_url}/100"
        response = requests.get(endpoint)
        assert response.status_code == 404