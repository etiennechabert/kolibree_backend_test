from django.db import models

class User(models.Model):
    first_name = models.CharField(blank=False)
    last_name = models.CharField(blank=False)
    date_of_birth = models.DateField(blank=False)
    email = models.EmailField(unique=True)
    password = models.CharField(blank=False)

class UserToken(models.Model):
    user_id = models.ForeignKey('User')
    token = models.UUIDField(auto=True)
    creation_dateTime = models.DateTimeField(auto_now=True)