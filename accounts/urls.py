from django.urls import path
from accounts import views

from .views import SignUp
app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', views.account_update, name='account_update')
]