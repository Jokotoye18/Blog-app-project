from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from django.contrib.auth import get_user_model
from .models import Article

from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class ArticleListView(ListView):
    template_name = 'articles/article_lists.html'
    context_object_name = 'articles'
    login_url = 'login'

    def get_queryset(self, *args):
        return Article.objects.order_by('-date_added')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    login_url = 'login'
    query_pk_and_slug = True
    slug_field = 'slug__iexact'
    

        

class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ['category', 'title', 'body']
    login_url = 'login'
    success_message = 'Article created successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ['title', 'body']
    login_url = 'login'
    query_pk_and_slug =True
    slug_field = 'slug__iexact'
    success_message = 'Article updated successfully'
    
    

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
              raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)





class ArticleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles:article_lists')
    login_url = 'login'
    query_pk_and_slug = True
    slug_field = 'slug__iexact'
    success_message = 'Article deleted successfully'
    
    

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
              raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)





    





