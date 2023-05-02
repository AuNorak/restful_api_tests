import unittest
import requests

class TestRestfulAPI(unittest.TestCase):
    BASE_URL = "https://api.restful-api.dev"

    def test_get_all_objects_returns_200(self):
        endpoint = f"{self.BASE_URL}/objects"
        response = requests.get(endpoint)
        self.assertEqual(response.status_code, 200)
    # tests the endpoint returns 200 for the full list of objects

    # def test_get_all_objects_as_unauthenticated_returns_403(self):
    #     endpoint = f"{self.BASE_URL}/objects/42"
    #     response = requests.get(endpoint)
    #     self.assertEqual(response.status_code, 403)
    # tests the endpoint returns 403 for a user without permission making get request

    def test_get_single_object_returns_200(self):
        endpoint = f"{self.BASE_URL}/objects/1"
        response = requests.get(endpoint)
        self.assertEqual(response.status_code, 200)
    # tests the endpoint returns 200 for a single objects in the list

    def test_get_multiple_object_returns_requested_objects(self):
        endpoint = f"{self.BASE_URL}/objects?id=1&id=4&id=5"
        response = requests.get(endpoint)
        data = response.json()
        expected_ids = ["1", "4", "5"]
        actual_ids = [obj['id'] for obj in data]
        self.assertCountEqual(actual_ids, expected_ids)
    # tests the endpoint returns 3 objects and the correct objects

    def test_get_multiple_same_object_returns_multiple_objects(self):
        endpoint = f"{self.BASE_URL}/objects?id=1&id=1&id=1"
        response = requests.get(endpoint)
        data = response.json()
        expected_ids = ["1","1","1"]
        actual_ids = [obj['id'] for obj in data]
        self.assertCountEqual(actual_ids, expected_ids)
    # tests the endpoint returns the same object multiple times when queried for the same object multiple times, I wasn't sure what the behaviour would be here and 
    # was looking for a breaking case, there may be an argument to remove this

    def test_get_all_objects_returns_list_of_objects(self):
        endpoint = f"{self.BASE_URL}/objects"
        response = requests.get(endpoint)
        data = response.json()
        self.assertIsInstance(data, list)
        for obj in data:
            self.assertIsInstance(obj, dict)
    # tests the endpoint returns 200 for the full list of objects

    def test_get_single_object_shape(self):
        endpoint = f"{self.BASE_URL}/objects/1"
        response = requests.get(endpoint)
        data = response.json()
        expected_keys = ['id', 'name', 'data']
        self.assertCountEqual(data.keys(), expected_keys)
    # tests the shape of the object is vaguely as expected

    def test_get_string_object_returns_404(self):
        endpoint = f"{self.BASE_URL}/objects/jon"
        response = requests.get(endpoint)
        self.assertEqual(response.status_code, 404)
    # tests the endpoint returns 404 for a string object

    def test_get_non_existent_object_returns_404(self):
        endpoint = f"{self.BASE_URL}/objects/100"
        response = requests.get(endpoint)
        self.assertEqual(response.status_code, 404)
    # tests the endpoint returns 404 for a single object not in the list

    # def test_post(self):
    #     pass  # Implement POST test here

    # def test_put(self):
    #     pass  # Implement PUT test here

    # def test_delete(self):
    #     pass  # Implement DELETE test here

if __name__ == "__main__":
    unittest.main()