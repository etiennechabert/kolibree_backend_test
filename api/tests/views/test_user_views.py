import unittest
from django.test import Client

class TestUserViews(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Welcome' in response.content, True)
