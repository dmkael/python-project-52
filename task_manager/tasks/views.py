from django.contrib import messages
from django.forms import Form
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.forms import TaskForm, TaskSearchForm
from task_manager.tasks.models import Task
from task_manager.mixins import LoginRequireMixin
from task_manager.tasks.mixins import TaskCreatorOnlyMixin


class TasksAbstractView(LoginRequireMixin):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')


class TasksIndexView(TasksAbstractView, ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = ['pk']

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("executor"). \
            prefetch_related("author").all()
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def get(self, request, *args, **kwargs):
        status = request.GET.get('status')
        executor = request.GET.get('executor')
        form = TaskSearchForm(request.GET) if status or executor else TaskSearchForm()
        tasks = self.get_queryset()
        if status:
            tasks = tasks.filter(status=status)
        if executor:
            tasks = tasks.filter(executor=executor)
        return render(request, self.template_name, {'tasks': tasks, 'form': form})


class TasksCreateView(TasksAbstractView, CreateView):
    template_name = 'tasks/create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Task has been created successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class TasksUpdateView(TasksAbstractView, UpdateView):
    template_name = 'tasks/update.html'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Task has been updated successfully.')
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form), status=400)


class TasksDeleteView(TaskCreatorOnlyMixin, TasksAbstractView, DeleteView):
    template_name = 'tasks/delete.html'
    form_class = Form
    permission_denied_message = _('Only author can delete a task')
    redirect_url = reverse_lazy('tasks')

    def get_success_url(self):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            _('Task has been deleted successfully.'))
        return super().get_success_url()
