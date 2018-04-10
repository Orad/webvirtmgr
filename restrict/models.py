from django.db import models
from django.contrib.auth.models import User


class RestrictInfrastructure(models.Model):
    is_hidden = models.BooleanField(default=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title