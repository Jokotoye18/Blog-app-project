from django.db import models
from django.conf import settings 
from django.urls import reverse
from django.contrib.auth import get_user_model


class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[str(self.pk)])                                                                                                                                           