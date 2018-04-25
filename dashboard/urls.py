from django.conf.urls import url

from dashboard.views import dashboard_view


urlpatterns = [
    url(r'^$', dashboard_view, name="dashboard"),
]