from django import forms
from task_manager.tasks.models import Task
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User


class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.get_full_name()}'


class TaskForm(forms.ModelForm):
    executor = CustomChoiceField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        error_messages = {"name": {"unique": _("A task with that name already exists.")}}
        widgets = {
            'status': forms.Select(),
            'executor': forms.Select(),
            'labels': forms.SelectMultiple(),
        }
