from django.conf.urls import include, url
from api.views import user

user_api_urls = [
    url(r'^$', user.users),
]

api_urls = [
    url(r'^users/', include(user_api_urls))
]