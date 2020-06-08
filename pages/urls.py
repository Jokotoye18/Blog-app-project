from django.urls import path
from .views import HomePage, ContactView, AboutPageView


app_name = 'pages'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about' )
]