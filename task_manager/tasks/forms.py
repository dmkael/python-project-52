from django import forms
from task_manager.tasks.models import Task
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.get_full_name()}'


class TaskForm(forms.ModelForm):
    executor = CustomChoiceField(
        queryset=get_user_model().objects.all(),
        required=False,
        label=_('Executor')
    )

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        error_messages = {"name": {"unique": _("A task with that name already exists.")}}
        widgets = {
            'status': forms.Select(),
            'executor': forms.Select(),
            'labels': forms.SelectMultiple(),
        }
