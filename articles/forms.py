from django import forms
from .models import Article
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ArticleCreateForm(forms.ModelForm):
    body = SummernoteTextField()

    class Meta:
        model = Article
        fields = ['title', 'category','tags', 'body']

        widgets = {
            'tags': forms.TextInput(attrs={'placeholder':'programming, coding, design etc'}),
            'body': SummernoteWidget()
        }

class ArticleUpdateForm(forms.ModelForm):
    body = SummernoteTextField()

    class Meta:
        model = Article
        fields = ['title', 'body']

        widgets = {
            'body': SummernoteWidget()
        }

