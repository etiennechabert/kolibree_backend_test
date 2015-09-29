from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False, null=False)