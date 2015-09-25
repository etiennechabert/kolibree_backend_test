from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=100)

class UserToken(models.Model):
    user = models.ForeignKey('User')
    token = models.UUIDField(auto_created=True)
    creation_dateTime = models.DateTimeField(auto_now=True)