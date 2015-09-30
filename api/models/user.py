from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import models, IntegrityError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from rest_framework import serializers
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_409_CONFLICT, HTTP_401_UNAUTHORIZED

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
            self.save()
        except ValidationError as e:
            return {
                'code' : HTTP_400_BAD_REQUEST,
                'data' : e.message_dict.items()
            }
        except IntegrityError as e:
            return {
                'code' : HTTP_409_CONFLICT,
                'data' : {'error' : e.args[1]}
            }
        return {
            'code' : HTTP_200_OK,
            'data' : 'new user created'
        }

    def get_valid_token(self):
        element = self.usertoken_set.all().order_by('-creation_dateTime').first()
        if element == None or element.is_valid() == False:
            return self.usertoken_set.create()
        return element

class UserAuth():
    def auth_process(self, params):
        try:
            user = User.objects.get(email=params['email'])
            if check_password(params['password'], user.password):
                return self.auth_process_success(user)
            return self.auth_process_fail()
        except ObjectDoesNotExist:
            return self.auth_process_fail()

    def auth_process_success(self, user):
        token = user.get_valid_token()
        return {
            'data' : {
                'text' : 'valid authentication',
                'token' : token.token.__str__()
            },
            'code' : HTTP_200_OK
        }

    def auth_process_fail(self):
        return {
            'data' : {
                'text' : 'Bad email/password',
            },
            'code' : HTTP_401_UNAUTHORIZED
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    date_of_birth = serializers.DateField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_of_birth')

@receiver(pre_save, sender=User)
def userPassword_encryption(sender, instance, *args, **kwargs):
    instance.password = make_password(instance.password)