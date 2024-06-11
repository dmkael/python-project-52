from django import forms
from task_manager.tasks.models import Task
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
        labels = {
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }

#
# class TaskSearchForm(forms.Form):
#     status = forms.ModelChoiceField(
#         queryset=Status.objects.all(),
#         widget=forms.Select,
#         required=False,
#         label=_('Status'),
#     )
#     executor = CustomChoiceField(
#         queryset=get_user_model().objects.all(),
#         widget=forms.Select,
#         required=False,
#         label=_('Executor'),
#     )
#     labels = forms.ModelChoiceField(
#         queryset=Label.objects.all(),
#         widget=forms.Select,
#         required=False,
#         label=_('Label'),
#     )
#     author = forms.BooleanField(required=False, label=_("Only your tasks"))
#
