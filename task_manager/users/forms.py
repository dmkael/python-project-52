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
