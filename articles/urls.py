from django.urls import path
from django.views.i18n import JavaScriptCatalog
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_lists'),
    path('new/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]