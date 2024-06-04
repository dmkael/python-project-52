from django.db import models
from django.utils import timezone


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
