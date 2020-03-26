from django.shortcuts import render
from .models import Article
from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ArticleListView(ListView):
    template_name = 'articles/article_lists.html'
    context_object_name = 'articles'

    def get_queryset(self, *args):
        return Article.objects.order_by('-date_added')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_article'] = Article.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = '__all__'
class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'body']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article:article_lists')
    

