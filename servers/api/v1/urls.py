from django.conf.urls import url
from django.conf.urls import include

from servers.api.v1 import views


urlpatterns = [
    url(r'^connections1/$', views.Connections1.as_view()),
    url(r'^connections2/$', views.Connections2.as_view()),
]