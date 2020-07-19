from django.urls import path
from .views import ApiRoot, BlogListApiView, BlogDetailApiView, ContactApiView, SubscribeApiView
urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),
    path('blogs/', BlogListApiView.as_view(), name='blog-api-list'),
    path('blogs/<slug:slug>/', BlogDetailApiView.as_view(), name='article-detail'),
    path('contact/', ContactApiView.as_view(), name='contact'),
    path('subscribe/', SubscribeApiView.as_view(), name='subscribe')
]