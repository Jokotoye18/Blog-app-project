from django.urls import path
from .views import BlogListApiView
urlpatterns = [
    path('blogs/', BlogListApiView.as_view(), name='blog-api-list'),
]