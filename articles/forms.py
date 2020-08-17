from django import forms
from .models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'truncated_content', 'category','tags', 'published', 'body']

        widgets = {
            'tags': forms.TextInput(attrs={'placeholder':'programming, coding, design etc'}),
            'published': forms.RadioSelect()
        }

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'truncated_content', 'category', 'tags', 'published', 'body']

    widgets = {
            'tags': forms.TextInput(attrs={'placeholder':'programming, coding, design etc'}),
            'published': forms.RadioSelect()
        }
