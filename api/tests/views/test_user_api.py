from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

factory = APIRequestFactory()
request = factory.get('/users')

class TestUserApi(APITestCase):

    def test_users_api_usage(self):
        response = self.client.get('/api/users/', {}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_create_user_good(self):
        data = {
            'first_name' : 'Etienne',
            'last_name' : 'Chabert',
            'email' : 'etienne.chabert@gmail.com',
            'password' : 'password',
            'date_of_birth' : '1990-11-18'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_create_user_false(self):
        data = {
            'first_name' : 'Etienne',
            'last_name' : 'Chabert',
            'email' : 'etienne.chabert@gmail.com',
            'password' : 'password',
            'date_of_birth' : '18-11-1990'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, 400)