from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
app_name = 'article'

urlpatterns = [
    path('posts/', ArticleListView.as_view(), name='article_lists'),
    path('post/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('posts/new/', ArticleCreateView.as_view(), name='article_create'),
    path('post/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('post/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete')
]