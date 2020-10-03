from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.core.exceptions import PermissionDenied 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import CreateView,  UpdateView
from django.views import View



from .forms import AccountUpdateForm
from .forms import CustomUserCreationForm

# Create your views here.

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class AccountUpdateView(LoginRequiredMixin, View):
    login_url = "login"
    def get(self, request, *args, **kwargs): 
        user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
        if user != request.user:
            raise PermissionDenied
        form = AccountUpdateForm(instance=user)
        context = {'user':user, 'form':form}
        return render(request, 'accounts/account_update.html', context)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
        form = AccountUpdateForm(request.POST or None, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect(reverse('pages:home'))
        messages.error(request, 'Invalid fields check the error below.')
        return render(request, 'accounts/account_update.html', {"form": form})
        


# class AccountUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = get_user_model()
#     form_class = AccountUpdateForm
#     template_name = 'accounts/account_update.html'
#     success_url = reverse_lazy('pages:home')
#     login_url = "login"
#     success_message = ""
    
#     def get_object(self):
#         return self.request.user
    
#     def dispatch(self, request, *args, **kwargs):
#         obj = self.get_object()
#         print(obj.username)
#         if obj.username != self.request.user.username:
#             raise PermissionDenied 
#         return super().dispatch(request, *args, **kwargs)
        
            

































