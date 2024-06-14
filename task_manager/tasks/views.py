from django.forms import Form
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.access_mixins import LoginRequireMixin
from task_manager.tasks.mixins import TaskAuthorOnlyMixin
from django_filters.views import FilterView
from task_manager.view_mixins import (
    CreateViewMixin,
    UpdateViewMixin,
    DeleteViewMixin,
    IndexViewMixin
)


class TaskAbstractView(LoginRequireMixin):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')


class TaskIndexView(TaskAbstractView, FilterView, IndexViewMixin):
    extra_context = {
        'url_name': 'task_create',
        'header': _('Tasks'),
        'button_text': _('Create task')
    }
    ordering = ['pk']


class TaskDetailView(TaskAbstractView, DetailView):
    template_name = 'tasks/detail.html'


class TaskCreateView(TaskAbstractView, CreateViewMixin):
    extra_context = {'button_text': _('Create'), 'header': _('Create task')}
    template_name = 'tasks/create.html'
    success_message = _('Task has been created successfully.')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(TaskAbstractView, UpdateViewMixin):
    extra_context = {'button_text': _('Edit'), 'header': _('Edit task')}
    template_name = 'tasks/update.html'
    success_message = _('Task has been updated successfully.')


class TaskDeleteView(TaskAuthorOnlyMixin, TaskAbstractView, DeleteViewMixin):
    extra_context = {'button_text': _('Yes, delete'), 'header': _('Delete task')}
    template_name = 'tasks/delete.html'
    success_message = _('Task has been deleted successfully.')
    success_url = reverse_lazy('tasks')
    form_class = Form
