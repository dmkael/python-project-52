from django.forms import Form
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task
from task_manager.access_mixins import LoginRequireMixin
from task_manager.tasks.mixins import TaskAuthorOnlyMixin
from task_manager.tasks.filters import TasksFilter
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


class TaskIndexView(TaskAbstractView, IndexViewMixin):
    template_name = 'tasks/index.html'
    ordering = ['pk']
    paginate_by = 3

    def get_queryset(self):
        queryset = Task.objects.prefetch_related('status', 'executor', 'author')
        # filtering through django-filters with ordering
        filter_data = TasksFilter(
            ordering=self.ordering,
            data=self.request.GET,
            queryset=queryset,
            request=self.request
        )
        # returning filtered queryset
        return filter_data.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adding filter to context
        if any(value for key, value in self.request.GET.items() if key != 'page'):
            context['filter'] = TasksFilter(
                ordering=self.ordering,
                data=self.request.GET,
                queryset=self.get_queryset(),
            )
        else:
            context['filter'] = TasksFilter()
        return context


class TaskDetailView(TaskAbstractView, DetailView):
    template_name = 'tasks/detail.html'


class TaskCreateView(TaskAbstractView, CreateViewMixin):
    template_name = 'tasks/create.html'
    success_message = _('Task has been created successfully.')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(TaskAbstractView, UpdateViewMixin):
    template_name = 'tasks/update.html'
    success_message = _('Task has been updated successfully.')


class TaskDeleteView(TaskAuthorOnlyMixin, TaskAbstractView, DeleteViewMixin):
    template_name = 'tasks/delete.html'
    success_message = _('Task has been deleted successfully.')
    form_class = Form
