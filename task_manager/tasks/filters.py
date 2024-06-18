import django_filters
from django import forms
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.forms import CustomChoiceField


class CustomExecutorFilter(django_filters.Filter):
    field_class = CustomChoiceField


class TasksFilter(django_filters.FilterSet):
    author = django_filters.BooleanFilter(
        widget=forms.CheckboxInput(),
        label=_("Only your tasks"),
        method="self_tasks",
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label")
    )
    executor = CustomExecutorFilter(
        queryset=User.objects.all(),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'author']

    # Redefining __init__ to add support ordering
    def __init__(self, ordering=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ordering = ordering

    def filter_queryset(self, queryset):
        # processing default filtering
        queryset = super().filter_queryset(queryset)
        # processing ordering for queryset if provided
        if self.ordering:
            ordering = (*self.ordering,)
            queryset = queryset.order_by(*ordering)
        return queryset

    def self_tasks(self, queryset, name, value):
        if name == 'author' and value:
            return queryset.filter(author__exact=self.request.user)
        return queryset
