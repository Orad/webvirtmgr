from django.db import models
from organizations.models import Organization


class Compute(models.Model):
    name = models.CharField(max_length=20)
    hostname = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=14, blank=True, null=True)
    type = models.IntegerField()
    organization = models.ForeignKey(Organization, related_name="compute_organization")

    def __unicode__(self):
        return self.hostname
