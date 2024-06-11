import django_filters
from django import forms
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _


class TasksFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status'),
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_('Executor')
    )
    author = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(),
        exclude=True,
        label=_("Only your tasks")
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Labels")
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'author']

    def filter_queryset(self, queryset):
        queryset = Task.objects.prefetch_related('status', 'executor', 'labels', 'author')
        return queryset

    @property
    def qs(self):
        tasks = super().qs
        if self.request.GET.get('author'):
            tasks = tasks.filter(author=self.request.user)
        return tasks.order_by('pk')
