import uuid
from django.utils import timezone
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import pre_save
from django.dispatch import receiver
from api.models.user import UserSerializer
from rest_framework import serializers
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

class UserToken(models.Model):
    TOKEN_VALIDITY_IN_DAYS = 0
    TOKEN_VALIDITY_IN_HOURS = 1
    TOKEN_VALIDITY_IN_MINUTES = 0
    TOKEN_VALIDITY_IN_SECONDS = 0

    user = models.ForeignKey('User', on_delete=CASCADE)
    token = models.UUIDField(primary_key=True)
    creation_dateTime = models.DateTimeField()

    # I overload the setup method to be able to assign a datetime on the first save
    def save(self, *args, **kwargs):
        if not self.creation_dateTime:
            self.creation_dateTime = timezone.now()
        return super(UserToken, self).save(*args, **kwargs)

    def is_valid(self):
        validity_delta = timedelta(
            days=self.TOKEN_VALIDITY_IN_DAYS,
            hours=self.TOKEN_VALIDITY_IN_HOURS,
            minutes=self.TOKEN_VALIDITY_IN_MINUTES,
            seconds=self.TOKEN_VALIDITY_IN_SECONDS
        )
        now = datetime.now(self.creation_dateTime.tzinfo)
        if self.creation_dateTime + validity_delta > now:
            return True
        return False

# Serialize class for userToken
class UserTokenSerializer(serializers.HyperlinkedModelSerializer):
    creation_dateTime = serializers.DateTimeField()

    class Meta:
        model = UserToken
        fields = ('token', 'creation_dateTime')

# The assignation of the token is handle by this callback
# We check the uniqueness of the randomized token by catching a DoesNotExist exception
@receiver(pre_save, sender=UserToken)
def userToken_attribution(sender, instance, *args, **kwargs):
    while instance.token == None:
        new_token = uuid.uuid4()
        try:
            UserToken.objects.get(token=new_token)
        except ObjectDoesNotExist:
            instance.token = new_token

# This helper method is used from the view
# Probably a bad idea to return HTML_RESPONSE code here,
# But I prefer to have short views
def get_user_for_token(data):
    try:
        token = UserToken.objects.get(token=data['token'])
        if token.is_valid():
            return {
                'data' : {
                    'user' : UserSerializer(token.user).data
                },
                'code' : HTTP_200_OK
            }
    except ObjectDoesNotExist as e:
        pass
    return {
        'data' : {
            'user' : None,
        },
        'code' : HTTP_400_BAD_REQUEST
    }
