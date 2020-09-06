from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=10)
    password = forms.CharField(label='password', max_length=255, widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=10)
    password = forms.CharField(label='password', max_length=255, widget=forms.PasswordInput())
