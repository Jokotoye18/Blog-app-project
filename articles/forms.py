from django import forms
from .models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category','tags', 'body']

        widgets = {
            'tags': forms.TextInput(attrs={'placeholder':'programming, coding, design etc'}),
        }

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']

        widgets = {
        }

