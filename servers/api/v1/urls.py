from django.conf.urls import url
from django.conf.urls import include

from servers.api.v1 import views


urlpatterns = [
    url(r'^connections/$', views.Connections.as_view()),
]