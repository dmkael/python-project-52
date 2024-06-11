import django_filters
from django import forms
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class SelfAuthorFilter(django_filters.Filter):
    def filter(self, qs, value):
        if not value:
            return qs
        parent = getattr(self, 'parent', None)
        request = getattr(parent, 'request', None) if parent else None
        return qs.filter(author__exact=request.user) if request else qs


class TasksFilter(django_filters.FilterSet):
    author = SelfAuthorFilter(
        widget=forms.CheckboxInput(),
        label=_("Only your tasks")
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_("Label")
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'author']

    def filter_queryset(self, queryset):
        queryset = Task.objects.prefetch_related('status', 'executor', 'author')
        return super().filter_queryset(queryset)
