from django.contrib import admin

from organizations.models import (Organization, UserOrganization)

admin.site.register(Organization)
admin.site.register(UserOrganization)