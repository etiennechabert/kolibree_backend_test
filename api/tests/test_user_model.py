from unittest import TestCase
from django.core.exceptions import ValidationError
from api.models.user import User

class userTestCase(TestCase):
    def test_user_model_fail(self):
        user = User.objects.create()
        with self.assertRaises(ValidationError): # Fully empty model
            user.clean_fields()

        user.first_name = 'Etienne'
        with self.assertRaises(ValidationError): # Just a first name
            user.clean_fields()

        user.last_name = 'Chabert'
        user.email = 'fake_mail'
        user.password = 'password'
        with self.assertRaises(ValidationError): # Invalid email
            user.clean_fields()

    def test_user_model_success(self):
        user = User.objects.create(first_name='Etienne', last_name='Chabert', email='etienne.chabert@gmail.com', password='pass')
        self.assertEqual(user.full_clean(), None)