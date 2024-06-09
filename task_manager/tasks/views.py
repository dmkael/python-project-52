from django.forms import Form
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.forms import TaskForm, TaskSearchForm
from task_manager.tasks.models import Task
from task_manager.mixins import LoginRequireMixin
from task_manager.tasks.mixins import TaskAuthorOnlyMixin
from task_manager.views import CreateFlashedView, UpdateFlashedView, DeleteFlashedView


class TaskAbstractView(LoginRequireMixin):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')


class TaskIndexView(TaskAbstractView, ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = ['pk']

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("executor"). \
            prefetch_related("author").prefetch_related('labels').all()
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get(self, request, *args, **kwargs):
        filters = {
            'status': request.GET.get('status'),
            'executor': request.GET.get('executor'),
            'labels': request.GET.get('labels'),
            'author': request.GET.get('self_tasks')
        }
        filters = {k: v for k, v in filters.items() if v}
        if filters.get('author'):
            filters['author'] = request.user.id
        form = TaskSearchForm(request.GET) if filters else TaskSearchForm()
        tasks = self.get_queryset().filter(**filters)
        return render(request, self.template_name, {'tasks': tasks, 'form': form})


class TaskDetailView(TaskAbstractView, DetailView):
    template_name = 'tasks/detail.html'


class TaskCreateView(TaskAbstractView, CreateFlashedView):
    template_name = 'tasks/create.html'
    valid_form_message = _('Task has been created successfully.')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(TaskAbstractView, UpdateFlashedView):
    template_name = 'tasks/update.html'
    valid_form_message = _('Task has been updated successfully.')


class TaskDeleteView(TaskAuthorOnlyMixin, TaskAbstractView, DeleteFlashedView):
    template_name = 'tasks/delete.html'
    valid_data_message = _('Task has been deleted successfully.')
    success_url = reverse_lazy('tasks')
    form_class = Form
