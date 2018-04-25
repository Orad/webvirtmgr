from datetime import date
from decimal import Decimal

from django.db import models

from servers.models import Compute


class Instance(models.Model):
    compute = models.ForeignKey(Compute)
    name = models.CharField(max_length=20)
    uuid = models.CharField(max_length=36)
    # display_name = models.CharField(max_length=50)
    # display_description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class RunningHistory(models.Model):
    instance = models.ForeignKey(Instance)
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

class RunningInstanceTime(models.Model):
    instance = models.ForeignKey(Instance)
    date = models.DateField(default=date.today)
    total_time = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal(0.0000))
    daily_time = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal(0.0000))