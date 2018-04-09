from django.contrib import admin

from restrict.models import (RestrictInfrastructure, UserDetail)

admin.site.register(RestrictInfrastructure)
admin.site.register(UserDetail)