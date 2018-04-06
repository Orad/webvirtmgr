from django.db import models

# Create your models here.

class RestrictInfrastructure(models.Model):
    is_hidden = models.BooleanField(default=False)
    title = models.CharField(max_length=255)

    def __str__(self):
    	return self.title