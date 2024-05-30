from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={
            'autofocus': '',
            'autocapitalize': "none",
            'autocomplete': 'username',
        })
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
        })
    )
