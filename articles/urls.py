from django.urls import path
from .models import Article
from .views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView, 
    DjangoArticleList, 
    PythonArticleList,
    OtherArticleList
)    


app_name = 'articles'

urlpatterns = [
    path('article/<slug:slug>-<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<slug:slug>-<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<slug:slug>-<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/create-new-article/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/django/', DjangoArticleList.as_view(), name='django_article_list'),
    path('articles/python/', PythonArticleList.as_view(), name='python_article_list'),
    path('articles/other/', OtherArticleList.as_view(), name='other_article_list'),
    path('articles/', ArticleListView.as_view(), name='article_lists'),
]