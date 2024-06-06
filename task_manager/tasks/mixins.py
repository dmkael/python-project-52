from django.contrib import messages
from task_manager.mixins import LoginRequireMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from task_manager.tasks.models import Task


class TaskCreatorOnlyMixin(LoginRequireMixin):
    redirect_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        if request.user.id == task.author.id:
            return super().dispatch(request, *args, **kwargs)

        if request.user.is_authenticated:
            messages.add_message(
                request,
                messages.ERROR,
                self.permission_denied_message
            )
            return redirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)
