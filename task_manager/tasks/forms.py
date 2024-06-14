from django import forms
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from task_manager.users.models import User
from django.utils.translation import gettext_lazy as _


class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.get_full_name()}  [{obj.username}]'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        error_messages = {"name": {"unique": _("A task with that name already exists.")}}
        widgets = {
            'status': forms.Select(),
            'executor': forms.Select(),
            'labels': forms.SelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        status_choices = Status.objects.all()
        executor_choices = User.objects.all()
        labels_choices = Label.objects.all()
        self.fields['status'].queryset = status_choices
        self.fields['executor'].queryset = executor_choices
        self.fields['labels'].queryset = labels_choices
