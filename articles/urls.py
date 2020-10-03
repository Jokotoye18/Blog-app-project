from django.urls import path
from django.views.decorators.cache import cache_page

from .feed import ArticlesFeed
from .models import Article
from .views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView, 
    CategoryListView, 
    SearchView,
    ArticleTagView,
    markdown_uploader,
)    


app_name = 'articles'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_lists'),
    path('article/<slug:slug>-<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<slug:slug>-<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<slug:slug>-<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/create-new-article/', ArticleCreateView.as_view(), name='article_create'),
    path('article/category/<title>/', CategoryListView.as_view(), name='category_list'),
    path('article/tags/<slug:tag_slug>/', ArticleTagView.as_view(), name='tags'),
    path('search/', SearchView.as_view(), name='search'),
    path('api/uploader/', markdown_uploader, name='markdown_uploader_page'),
    path('feed/rss/', ArticlesFeed(), name='articles_feed')
]