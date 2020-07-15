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


import os
import json
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from martor.utils import LazyEncoder




class ArticleListView(ListView):
    template_name = 'articles/article_lists.html'
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-date_added')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.order_by('title')
        context['latest_article'] = self.get_queryset()[:5]
        return context
    

class CategoryListView(ListView):
    context_object_name = 'category_list'
    template_name = 'articles/category_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(category__title=self.kwargs['title']).order_by('-date_added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = self.get_queryset().filter(category__title=self.kwargs['title'])
        context['category'] = categories.only('category__title').first()
        context['articles'] = Article.objects.order_by('-date_added')[:5]
        return context

    

class ArticleTagView(ListView):
    model = Article
    template_name = 'tag.html'
    context_object_name = 'article_tags'

    def get_queryset(self):
        return Article.objects.filter(tags__slug=self.kwargs['tag_slug']).order_by('-date_added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.order_by('-date_added')[:5]
        context['tagged'] = self.get_queryset().filter(tags__slug__icontains=self.kwargs['tag_slug']).only('tags__slug').first()
        return context
        
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    query_pk_and_slug = True

        
class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articles/article_new.html'
    login_url = 'login'
    redirect_field_name = 'next'
    success_message = 'Article created successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'articles/article_update.html'
    context_object_name = 'article'
    login_url = 'login'
    redirect_field_name = 'next'
    query_pk_and_slug =True
    success_message = 'Article updated successfully'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
              raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)




#LoginRequiredMixin
class ArticleDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles:article_lists')
    login_url = 'login'
    redirect_field_name = 'next'
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
        if q is None :
            return None
        elif  q  :
            return []
        else:
            search_list = queryset.filter(
                Q(title__icontains=q) | Q(body__icontains=q)
            )
            return search_list


@login_required
def markdown_uploader(request):
    """
    Makdown image upload for locale storage
    and represent as json to markdown editor.
    """
    if request.method == 'POST' and request.is_ajax():
        if 'markdown-image-upload' in request.FILES:
            image = request.FILES['markdown-image-upload']
            image_types = [
                'image/png', 'image/jpg',
                'image/jpeg', 'image/pjpeg', 'image/gif'
            ]
            if image.content_type not in image_types:
                data = json.dumps({
                    'status': 405,
                    'error': _('Bad image format.')
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                to_MB = settings.MAX_IMAGE_UPLOAD_SIZE / (1024 * 1024)
                data = json.dumps({
                    'status': 405,
                    'error': _('Maximum image file is %(size) MB.') % {'size': to_MB}
                }, cls=LazyEncoder)
                return HttpResponse(
                    data, content_type='application/json', status=405)

            img_uuid = "{0}-{1}".format(uuid.uuid4().hex[:10], image.name.replace(' ', '-'))
            tmp_file = os.path.join(settings.MARTOR_UPLOAD_PATH, img_uuid)
            def_path = default_storage.save(tmp_file, ContentFile(image.read()))
            img_url = os.path.join(f'https://jokotoye-blog.s3.us-east-2.amazonaws.com{settings.MEDIA_URL}', def_path)
            data = json.dumps({
                'status': 200,
                'link': img_url,
                'name': image.name
            })
            return HttpResponse(data, content_type='application/json')
        return HttpResponse(_('Invalid request!'))
    return HttpResponse(_('Invalid request!'))