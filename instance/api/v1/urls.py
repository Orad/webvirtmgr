from django.conf.urls import url
from django.conf.urls import include

from instance.api.v1 import views


urlpatterns = [
    url(r'^change_status/(?P<host_id>\d+)/$', views.ChangeStatus.as_view() ),
    url(r'^vm_snapshots/(?P<host_id>\d+)/$', views.VMSnapshots.as_view() ),
    url(r'^save_event/$', views.SaveEvent.as_view() ),
]