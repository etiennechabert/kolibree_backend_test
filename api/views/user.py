from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from api.models.user import User, UserSerializer, UserAuth
from api.models.user_token import get_user_for_token

def users_usage():
    return {
                'methods' : {
                    'api/users' : {
                        'methods' : {
                            'GET' : 'Access to this Usage',
                            'POST' : 'Create the new user'
                        }
                    },
                    'api/users/auth' : {
                        'methods' : {
                            'POST' : 'Try to authenticate (get a token)'
                        }
                    },
                    'api/users/retrieve' : {
                        'methods' : {
                            'POST' : 'Access user\'s data according to the token (require a token)'
                        }
                    },

                }
            }

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        return Response(users_usage(), HTTP_200_OK)
    elif request.method == 'POST':
        response = User().handle_create(request.data)
        return Response(response['data'], response['code'])

@api_view(['POST'])
def auth(request):
    data = request.data
    response = UserAuth().auth_process(data)
    return Response(response['data'], response['code'])

@api_view(['POST'])
def retrieve(request):
    data = request.data
    response = get_user_for_token(data)
    return Response(response['data'], response['code'])
