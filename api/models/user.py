from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK


class User(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False, null=False)

    def handle_create(self, data):
        for k, v in data.items():
            setattr(self, k, v)
        try:
            self.clean_fields()
        except ValidationError as e:
            return {
                'code' : HTTP_400_BAD_REQUEST,
                'data' : e.message_dict.items()
            }
        self.save()
        return {
            'code' : HTTP_200_OK,
            'data' : 'new user created'
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    date_of_birth = serializers.DateField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_of_birth')
