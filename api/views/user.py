from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from api.models.user import User, UserSerializer

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        return Response(
            {
                'methods' : {
                    'api/users' : {
                        'methods' : {
                            'GET' : 'Access to this Usage',
                            'POST' : 'Create the new user'
                        }
                    },
                    'api/user' : {
                        'methods' : {
                            'POST' : 'Try to authenticate (get a token)'
                        }
                    },
                    'api/user/:token' : {
                        'methods' : {
                            'GET' : 'Access user\'s data according to the token (require a token)'
                        }
                    },

                }
            }, HTTP_200_OK
        )
    elif request.method == 'POST':
        response = User().handle_create(request.data)
        return Response(response['data'], response['code'])


