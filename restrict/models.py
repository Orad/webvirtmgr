from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up

from organizations.models import Organization, UserOrganization


class RestrictInfrastructure(models.Model):
    is_hidden = models.BooleanField(default=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

@receiver(user_signed_up)
def user_signed_up_(request, user, **kwargs):
    organization = Organization(name = str(user.username)+"_organization")
    organization.save()

    user_organization = UserOrganization(user = user,organization = organization)
    user_organization.save()
