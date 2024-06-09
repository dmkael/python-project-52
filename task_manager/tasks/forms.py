from django import forms
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.get_full_name()}  [{obj.username}]'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "status": _("Status"),
            "executor": _("Executor"),
            "labels": _("Labels")
        }
        error_messages = {"name": {"unique": _("A task with that name already exists.")}}
        widgets = {
            'status': forms.Select(),
            'executor': forms.Select(),
            'labels': forms.SelectMultiple(),
        }


class TaskSearchForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        widget=forms.Select,
        required=False,
        label=_("Status"),
    )
    executor = CustomChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.Select,
        required=False,
        label=_("Executor")
    )
    labels = forms.ModelChoiceField(
        queryset=Label.objects.all(),
        widget=forms.Select,
        required=False,
        label=_('Labels')
    )
    self_tasks = forms.BooleanField(required=False, label=_("Only your tasks"))
