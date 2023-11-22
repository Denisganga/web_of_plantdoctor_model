# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Enter a valid email address.')

    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']
