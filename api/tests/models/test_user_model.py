from unittest import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from api.models.user import User

class userTestCase(TestCase):
    def setUp(self):
        self.user = User()

    def test_user_model_fail(self):
        with self.assertRaises(ValidationError): # Fully empty model
            self.user.clean_fields()

        self.user.first_name = 'Etienne'
        with self.assertRaises(ValidationError): # Just a first name
            self.user.clean_fields()

        self.user.last_name = 'Chabert'
        self.user.email = 'fake_mail'
        self.user.password = 'password'
        with self.assertRaises(ValidationError): # Invalid email
            self.user.clean_fields()

    def test_user_model_success(self):
        User.objects.all().delete();
        user = User.objects.create(first_name='Etienne', last_name='Chabert', email='etienne.chabert@gmail.com', password='pass', date_of_birth='1990-11-18')
        self.assertEqual(user.full_clean(), None)

    def test_user_model_duplicate(self):
        User.objects.all().delete();
        with self.assertRaises(IntegrityError):
            user = User.objects.create(first_name='Etienne', last_name='Chabert', email='etienne.chabert@gmail.com', password='pass', date_of_birth='1990-11-18')
            user = User.objects.create(first_name='Etienne', last_name='Chabert', email='etienne.chabert@gmail.com', password='pass', date_of_birth='1990-11-18')
