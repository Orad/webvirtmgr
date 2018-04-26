from django.conf.urls import url

from users.views import user_info_view, account_deactivate_view


urlpatterns = [
    url(r'^userinfo/$', user_info_view, name="userinfo"),
    url(r'^deactivate/$', account_deactivate_view, name="account_deactivate"),
]