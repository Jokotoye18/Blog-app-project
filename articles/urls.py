from django.urls import path
from .models import Article
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView


app_name = 'articles'

urlpatterns = [
    path('article/<slug:slug>-<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<slug:slug>-<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<slug:slug>-<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/new/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/', ArticleListView.as_view(), name='article_lists'),
]