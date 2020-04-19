from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages 
from django.urls import reverse_lazy
from accounts.models import User
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


def account_update(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            messages.success(request, f"Your accounts has been updated succesfully")
            return redirect('pages:home')

        else:
            messages.warning(request, 'Please correct the error  below')

    else:
        form = AccountUpdateForm(instance=request.user) 
    context = {'form':form}
    return render(request, 'accounts/account_update.html', context)


