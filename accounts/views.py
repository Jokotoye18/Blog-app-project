from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import AccountUpdateForm
from django.http import HttpResponseRedirect




from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from .forms import CustomUserCreationForm

# Create your views here.

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'



class AccountUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = AccountUpdateForm
    template_name = 'accounts/account_update.html'
    success_url = reverse_lazy('pages:home')
    login_url = "login"
    success_message = "Profile updated successfully!"
    
    def get_object(self):
        return self.request.user
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.username)
        if obj.username != self.request.user.username:
            raise PermissionDenied 
        return super().dispatch(request, *args, **kwargs)
        
            

































