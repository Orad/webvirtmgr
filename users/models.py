from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userinfo")
    phone_number = models.CharField(max_length=10, blank=True)
