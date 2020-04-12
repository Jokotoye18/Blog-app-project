from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from django.contrib.auth import get_user_model
from .models import Article

from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class ArticleListView( ListView):
    template_name = 'articles/article_lists.html'
    context_object_name = 'articles'
    login_url = 'login'

    def get_queryset(self, *args):
        return Article.objects.order_by('-date_added')


class ArticleDetailView( DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    login_url = 'login'
        


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ['title', 'body']
    login_url = 'login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'body']
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
              raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article:article_lists')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
              raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)





    





