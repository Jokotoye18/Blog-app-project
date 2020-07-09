from django.urls import path
from .models import Article
from .import views
from .views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView, 
    CategoryListView, 
    SearchView,
    ArticleTagView
)    


app_name = 'articles'

urlpatterns = [
    path('article/<slug:slug>-<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<slug:slug>-<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<slug:slug>-<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/create-new-article/', ArticleCreateView.as_view(), name='article_create'),
    path('article/category/<title>/', CategoryListView.as_view(), name='category_list'),
    path('article/tagged/<slug:tag_slug>/', ArticleTagView.as_view(), name='tags'),
    path('articles/', ArticleListView.as_view(), name='article_lists'),
    path('search/', SearchView.as_view(), name='search'),
]