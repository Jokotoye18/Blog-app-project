from django import forms
from .models import Contact, Subscribe

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {'name':'', 'email': '', 'message': ''}
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Name'}), 
            'email':forms.TextInput(attrs={'placeholder':'Your mail e.g johnpowell12@gmail.com'}),
            'message':forms.Textarea(attrs={'placeholder':'Your message'}),
        }

class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ['email']
        labels = {'email':''}
        widgets = {'email':forms.TextInput(attrs={'placeholder':'mikedean@gmail.com'})}