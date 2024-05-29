from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'autocomplete': 'new-password'
        }),
        help_text=_('<ul><li>Your password must contain at least 3 characters.</li><ul>')
    )

    password2 = forms.CharField(
        error_messages={
            'min_length': _('The entered password is too short. It must contain at least 3 characters.')
        },
        min_length=3,
        label=_('Confirm password'),
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Confirm password'),
            'autocomplete': 'new-password'
        }),
        help_text=_('To confirm, please enter your password again.')
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', _('The entered passwords do not match.'))
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user
