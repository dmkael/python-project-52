from task_manager.mixins import LimitedPermissionsMixin, LoginRequireMixin
from django.urls import reverse_lazy
from task_manager.tasks.models import Task
from django.utils.translation import gettext_lazy as _


class TaskAuthorOnlyMixin(LimitedPermissionsMixin):
    redirect_url = reverse_lazy('tasks')
    permission_denied_message = _('Only author can delete a task')
    have_permission = False

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        if request.user.id == task.author.id:
            self.have_permission = True
        return super().dispatch(request, *args, **kwargs)
