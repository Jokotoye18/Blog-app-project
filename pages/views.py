from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ContactForm, SubscribeForm
from django.views.generic import View, CreateView

class HomePage(View):
    def get(self, request, *args, **kwargs):
        form = SubscribeForm()
        context = {'form':form}
        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            messages.info(request, 'Suscribed successfully')
            form.save()
        return redirect('pages:home')

    
    
    #template_name = 'home.html'

class ContactView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_message = 'Your message has been received.'
