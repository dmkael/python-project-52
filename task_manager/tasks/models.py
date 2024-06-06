from django.db import models
from django.utils import timezone
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model


# Create your models here.
class Task(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        related_name='tasks_author',
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=False, blank=False)
    executor = models.ForeignKey(
        get_user_model(),
        related_name='tasks_executor',
        null=True, blank=True,
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
