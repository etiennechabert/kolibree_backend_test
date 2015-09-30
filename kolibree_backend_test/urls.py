from django.conf.urls import include, url
from api.views import index
from api.urls import api_urls

urlpatterns = [
    url(r'^$', index.index),
    url(r'^api/', include(api_urls)),
]
