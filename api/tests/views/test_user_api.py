from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from api.models import User

factory = APIRequestFactory()
request = factory.get('/users')

class TestUserApiCreate(APITestCase):
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
        self.assertEqual(response.status_code, 200) # good test

        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, 409) # duplicate user test

    def test_create_user_false(self):
        data = {
            'first_name' : 'Etienne',
            'last_name' : 'Chabert',
            'email' : 'etienne.chabert@gmail.com',
            'password' : 'password',
            'date_of_birth' : '18-11-1990'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, 400) # failing test

class TestUserApiAuth(APITestCase):
    def setUp(self):
        self.user = User(first_name='Etienne',last_name='Chabert',email='etienne.chabert@gmail.com',password='password',date_of_birth='1990-11-18').save()

    def test_user_valid_authentication(self):
        data = {
            'email' : 'etienne.chabert@gmail.com',
            'password' : 'password'
        }
        response = self.client.post('/api/users/auth', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('valid authentication' in response.content, True)
        self.assertEqual('token' in response.content, True)

    def test_user_bad_password(self):
        data = {
            'email' : 'etienne.chabert@gmail.com',
            'password' : 'pass'
        }
        response = self.client.post('/api/users/auth', data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual('Bad email/password' in response.content, True)

    def test_user_bad_email(self):
        data = {
            'email' : 'etinne.chabert@gmail.com',
            'password' : 'password'
        }
        response = self.client.post('/api/users/auth', data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual('Bad email/password' in response.content, True)
