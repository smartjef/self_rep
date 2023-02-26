from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AdvocateSignUpForm(UserCreationForm):
    field = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    username = forms.CharField(max_length=50, required=True)
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'field')
