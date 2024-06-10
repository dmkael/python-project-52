from django.db import models
from django.utils import timezone
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name='tasks_author',
        on_delete=models.PROTECT,
    )
    name = models.CharField(
        _("Name"),
        max_length=255,
        unique=True,
        null=False, blank=False)
    description = models.TextField(_("Description"), null=True, blank=True)
    status = models.ForeignKey(
        Status,
        related_name='tasks',
        null=False, blank=False,
        on_delete=models.CASCADE,
    )
    labels = models.ManyToManyField(Label, related_name='tasks', blank=True)
    executor = models.ForeignKey(
        get_user_model(),
        related_name='tasks_executor',
        null=True, blank=True,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
