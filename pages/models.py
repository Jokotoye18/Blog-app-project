from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=1500)

    class Meta:

        ordering = ['id']


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('pages:home')


class Subscribe(models.Model):
    email = models.EmailField(max_length=50)

    class Meta:

        ordering = ['id']
    def __str__(self):
        return self.email
