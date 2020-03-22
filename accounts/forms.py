from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm):
    class Meta():
        model = User
        fields = ['username', 'email']
