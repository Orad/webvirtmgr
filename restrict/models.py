from django.db import models
from django.contrib.auth.models import User


class RestrictInfrastructure(models.Model):
    is_hidden = models.BooleanField(default=False)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_detail")
    token = models.TextField(blank=True, null=True)