from django import forms
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        error_messages = {'name': {
            "unique": _("A status with that name already exists.")
        }}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': True})
