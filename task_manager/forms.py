from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
