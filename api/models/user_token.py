import uuid
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import pre_save
from django.dispatch import receiver

class UserToken(models.Model):
    TOKEN_VALIDITY_IN_DAYS = 0
    TOKEN_VALIDITY_IN_HOURS = 1
    TOKEN_VALIDITY_IN_MINUTES = 0
    TOKEN_VALIDITY_IN_SECONDS = 0

    user = models.ForeignKey('User', on_delete=CASCADE)
    token = models.UUIDField(primary_key=True)
    creation_dateTime = models.DateTimeField(auto_now=True)

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

############## CALLBACKS FOR UserToken ############

@receiver(pre_save, sender=UserToken)
def userToken_attribution(sender, instance, *args, **kwargs):
    while instance.token == None:
        new_token = uuid.uuid4()
        try:
            UserToken.objects.get(token=new_token)
        except ObjectDoesNotExist:
            instance.token = new_token
