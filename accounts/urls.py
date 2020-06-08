from django.urls import path

from .views import SignUp, AccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile-update/', AccountUpdateView.as_view(), name='account_update'),
]