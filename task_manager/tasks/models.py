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
        verbose_name=_('Author'),
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False, blank=False,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name=_("Description"),
    )
    status = models.ForeignKey(
        Status,
        related_name='tasks',
        null=False, blank=False,
        on_delete=models.PROTECT,
        verbose_name=_('Status'),
    )
    labels = models.ManyToManyField(
        Label,
        related_name='tasks',
        blank=True,
        verbose_name=_('Labels'),
    )
    executor = models.ForeignKey(
        get_user_model(),
        related_name='tasks_executor',
        null=True, blank=True,
        on_delete=models.PROTECT,
        verbose_name=_('Executor'),
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
