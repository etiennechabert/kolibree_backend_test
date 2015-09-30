from unittest import TestCase
from datetime import timedelta
from api.models.user import User
from api.models.user_token import UserToken

class userTokenTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.get(first_name='Etienne', last_name='Chabert')
        self.user.usertoken_set.all().delete()

    def test_unique_token(self):
        self.user.usertoken_set.create()
        self.user.usertoken_set.create()
        self.assertEqual(self.user.usertoken_set.count(), 2)

    def test_get_valid_token(self):
        self.user.get_valid_token()
        self.user.get_valid_token()
        self.assertEqual(self.user.usertoken_set.count(), 1)

    def test_valid_token(self):
        token = self.user.usertoken_set.create()
        self.assertEqual(token.is_valid(), True)

    def test_exipired_token(self):
        token = self.user.usertoken_set.create()
        token.creation_dateTime = token.creation_dateTime - timedelta(
            days=2*UserToken.TOKEN_VALIDITY_IN_DAYS,
            hours=2*UserToken.TOKEN_VALIDITY_IN_HOURS,
            minutes=2*UserToken.TOKEN_VALIDITY_IN_MINUTES,
            seconds=2*UserToken.TOKEN_VALIDITY_IN_SECONDS
        )
        self.assertEqual(token.is_valid(), False)