from django.shortcuts import render, redirect
from django.conf import settings
from .models import Contact 
from django.core.mail import  send_mail
from django.template.loader import get_template
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ContactForm, SubscribeForm
from django.views.generic import View, CreateView, TemplateView

class HomePage(View):
    def get(self, request, *args, **kwargs):
        form = SubscribeForm()
        context = {'form':form}
        return render(request, 'home.html', context)


    def post(self, request, *args, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            to_email = request.POST['email']
            subject = 'Subscription Form Received'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [to_email]
            subscribe_message = f'{to_email}! Thanks for subscribing to our newsletter. We promise to always update you on our next post.'
            send_mail(subject, subscribe_message, from_email, to_email, fail_silently=True)
            messages.info(request, 'Suscribed successfully')
            form.save()
        return redirect('pages:home')

    
    
    #template_name = 'home.html'

class ContactView(SuccessMessageMixin, View):
    success_message = 'Your message has been received.'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form':form}
        return render(request, 'contact.html', context)
    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'contact message received')
        return redirect('pages:contact')
        


class AboutPageView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        form = SubscribeForm()
        context = {'form':form}
        return render(request, 'about.html', context)

    def post(self, request, *args, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            to_email = request.POST['email']
            subject = 'Subscription Form Received'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [to_email]
            subscribe_message = f'{to_email}! Thanks for subscribing to our newsletter. We promise to always update you on our next post.'
            send_mail(subject, subscribe_message, from_email, to_email, fail_silently=True)
            messages.info(request, 'Suscribed successfully')
            form.save()
        return redirect('pages:about')





