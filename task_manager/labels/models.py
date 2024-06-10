from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Label(models.Model):
    name = models.CharField(_("Name"), max_length=255, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
