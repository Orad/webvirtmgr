from hotqueue import HotQueue
from webvirtmgr.utils.util import get_connection
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

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

@receiver(post_save, sender=Compute)
def post_save_handler(sender, instance, created, *args, **kwargs):
    data = get_connection(instance.type, instance.login, instance.hostname)
    queue = HotQueue("ComputeQueue")
    if created:
        queue.put({'event': "Created", 'data':data})
    else:
        queue.put({'event': "updated", 'data':data})

@receiver(post_delete, sender=Compute)
def post_delete_handler(sender, instance, *args, **kwargs):
    if instance:
        data = get_connection(instance.type, instance.login, instance.hostname)
        queue = HotQueue("ComputeQueue")
        queue.put({'event': "Deleted", 'data':data})