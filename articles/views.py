from django.shortcuts import render,get_object_or_404,redirect
from .models import Article
from django.contrib.auth import get_user_model
from .models import Article, Category
from django.db.models import Q
from .forms import ArticleCreateForm, ArticleUpdateForm
from django.urls import reverse_lazy,reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.core.exceptions import PermissionDenied 
from django.views.generic import ListView, DetailView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class ArticleListView(ListView):
    template_name = 'articles/article_lists.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-date_added')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('title')
        context['latest_article'] = Article.objects.order_by('-date_added')[:5]
        return context
    

class CategoryListView(ListView):
    context_object_name = 'category_list'
    template_name = 'articles/category_list.html'
    paginate_by = 2

    def get_query(self):
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_query().filter(category__title=self.kwargs['title']).only('category__title').first()
        context['articles'] = self.get_query().order_by('-date_added')[:5]
        print(context['category'])
        return context

    def get_queryset(self):
        return self.get_query().filter(category__title=self.kwargs['title']).order_by('-date_added')

class ArticleTagView(ListView):
    model = Article
    template_name = 'tag.html'
    context_object_name = 'article_tags'

    def get_query(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.get_query().order_by('-id')
        context['tagged'] = self.get_query().filter(tags__slug=self.kwargs['tag_slug']).only('tags__slug').first()
        print(context['tagged'])
        return context

    def get_queryset(self):
        return self.get_query().filter(tags__slug=self.kwargs['tag_slug']).order_by('-date_added')

        
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    query_pk_and_slug = True

        

class ArticleCreateView(SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_new.html'
    # login_url = 'login'
    success_message = 'Article created successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'articles/article_update.html'
    context_object_name = 'article'
    # login_url = 'login'
    query_pk_and_slug =True
    success_message = 'Article updated successfully'
    
    

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
              raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)




#LoginRequiredMixin
class ArticleDeleteView(SuccessMessageMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles:article_lists')
    # login_url = 'login'
    context_object_name = 'article'
    query_pk_and_slug = True
    success_message = 'Article deleted successfully'
    
    

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
              raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)



class SearchView(ListView):
    model = Article
    context_object_name = 'search_list'
    template_name = 'search.html'
    
    def get_queryset(self):
        queryset = Article.objects.all()
        q = self.request.GET.get('q', None)
        print(q)
        if q is None :
            return None
        elif q == '':
            return []
        else:
            search_list = queryset.filter(
                Q(title__icontains=q) | Q(body__icontains=q)
            )
            return search_list