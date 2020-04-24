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
    queryset = Article.objects.order_by('-date_added')
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_article'] = Article.objects.order_by('-date_added')[:4]
        context['django_category_count'] = Article.objects.filter(category__iexact='django').count()
        context['python_category_count'] = Article.objects.filter(category__iexact='python').count()
        context['other_category_count'] = Article.objects.filter(category__iexact='other').count()
        return context

class DjangoArticleList(ListView):
    model = Article
    context_object_name = 'django_list'
    template_name = 'articles/django_article_list.html'
    paginate_by = 8

    def get_queryset(self):
        self.query = Article.objects.filter(category__iexact='django').order_by('-date_added')
        return self.query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['django_latest'] = Article.objects.filter(category__iexact='django').order_by('-date_added')[:4]
        return context

class PythonArticleList(ListView):
    model = Article
    context_object_name = 'python_list'
    template_name = 'articles/python_article_list.html'
    paginate_by = 8

    def get_queryset(self):
        self.query = Article.objects.filter(category__iexact='python').order_by('-date_added')
        return self.query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['python_latest'] = Article.objects.filter(category__iexact='python').order_by('-date_added')[:4]
        return context


class OtherArticleList(ListView):
    model = Article
    context_object_name = 'other_list'
    template_name = 'articles/other_article_list.html'
    paginate_by = 8

    def get_queryset(self):
        self.query = Article.objects.filter(category__iexact='other').order_by('-date_added')
        return self.query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_latest'] = Article.objects.filter(category__iexact='other').order_by('-date_added')[:4]
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
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





    





