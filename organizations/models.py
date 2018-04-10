from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class UserOrganization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizations")
    organization = models.ForeignKey(Organization, related_name="user_organization")

    def __str__(self):
        return "%s %s"%(self.user.username, self.organization.name)