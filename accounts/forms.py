from django import forms
from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email',]
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'username'}),
            'email':forms.TextInput(attrs={'placeholder':'Your Mail: e.g johndove@gmail.com'}),
        }

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields  = ['username', 'email']


class AccountUpdateForm(forms.ModelForm):
    
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'username', 'email']

