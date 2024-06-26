from django import forms
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        error_messages = {'name': {
            "unique": _("A label with that name already exists.")
        }}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': True})
