from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(_('First name'), max_length=50, blank=False, null=False)
    last_name = models.CharField(_('Last name'), max_length=50, blank=False, null=False)
