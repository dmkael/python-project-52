from django.contrib.auth import get_user_model
from django.contrib.auth.forms import BaseUserCreationForm


class UserCreateForm(BaseUserCreationForm):

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.pop('autofocus')
