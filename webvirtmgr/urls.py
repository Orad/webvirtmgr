from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'servers.views.index', name='index'),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    url(r'^servers/$', 'servers.views.servers_list', name='servers_list'),
    url(r'^infrastructure/$', 'servers.views.infrastructure', name='infrastructure'),
    url(r'^host/(\d+)/$', 'hostdetail.views.overview', name='overview'),
    url(r'^create/(\d+)/$', 'create.views.create', name='create'),
    url(r'^storages/(\d+)/$', 'storages.views.storages', name='storages'),
    url(r'^storage/(\d+)/([\w\-\.]+)/$', 'storages.views.storage', name='storage'),
    url(r'^networks/(\d+)/$', 'networks.views.networks', name='networks'),
    url(r'^network/(\d+)/([\w\-\.]+)/$', 'networks.views.network', name='network'),
    url(r'^interfaces/(\d+)/$', 'interfaces.views.interfaces', name='interfaces'),
    url(r'^interface/(\d+)/([\w\.\:]+)/$', 'interfaces.views.interface', name='interface'),
    url(r'^instance/(\d+)/([\w\-\.\_]+)/$', 'instance.views.instance', name='instance'),
    url(r'^instances/(\d+)/$', 'instance.views.instances', name='instances'),
    url(r'^secrets/(\d+)/$', 'secrets.views.secrets', name='secrets'),
    url(r'^console/$', 'console.views.console', name='console'),
    url(r'^info/hostusage/(\d+)/$', 'hostdetail.views.hostusage', name='hostusage'),
    url(r'^info/insts_status/(\d+)/$', 'instance.views.insts_status', name='insts_status'),
    url(r'^info/inst_status/(\d+)/([\w\-\.]+)/$', 'instance.views.inst_status', name='inst_status'),
    url(r'^info/instusage/(\d+)/([\w\-\.]+)/$', 'instance.views.instusage', name='instusage'),
    url(r'^key_console/$', 'console.views.key_console', name='key_console'),
    url(r'^generate_api_key/$', 'console.views.generate_api_key', name='generate_api_key'),
    url(r'^delete_api_key/$', 'console.views.delete_api_key', name='delete_api_key'),
    url(r'^signup/','allauth.account.views.signup', name="account_signup" ),
    url(r'^login/$', 'allauth.account.views.login', name="account_login"),
    url(r'^logout/$', 'allauth.account.views.logout', name="account_logout"),
    url(r'^confirm-email/$', 'allauth.account.views.email_verification_sent', name="account_email_verification_sent"),
    url(r'^confirm-email/(?P<key>\w+)/$', 'allauth.account.views.confirm_email', name="account_confirm_email"),
    url(r'^confirm_email/(?P<key>\w+)/$', RedirectView.as_view(url='/accounts/confirm-email/%(key)s/')),
    url(r"^password/reset/$", 'allauth.account.views.password_reset', name="account_reset_password"),
    url(r"^password/reset/done/$", 'allauth.account.views.password_reset_done', name="account_reset_password_done"),
    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$", 'allauth.account.views.password_reset_from_key', name="account_reset_password_from_key"),
    url(r"^password/reset/key/done/$", 'allauth.account.views.password_reset_from_key_done', name="account_reset_password_from_key_done"),
    url(r'^accounts/', include('allauth.socialaccount.providers.github.urls')),
    url(r'^social/signup/$', 'allauth.socialaccount.views.signup', name='socialaccount_signup'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^api/', include('instance.api.v1.urls')),
    url(r'^api/', include('servers.api.v1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
