from django.db import models
from django.utils.html import mark_safe
from markdown import markdown
from django.conf import settings 
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator, XtdCommentModerator
from martor.models import MartorField
from django.utils.html import mark_safe
from markdown import markdown
from rest_auth import serializers



#from django_comments.moderation import CommentModerator
#from django_comments_xtd.moderation import moderator, XtdCommentModerator


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    objects = models.Manager()

    class Meta:
        ordering = ['title']
        verbose_name_plural  = 'categories'

    def __str__(self):
        return self.title



class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    body = MartorField()
    tags = TaggableManager()
    TAGGIT_CASE_INSENSITIVE = True
    slug = models.SlugField(max_length=150, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)


    objects = models.Manager() 

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[self.slug, (self.pk)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_body_as_markdown(self):
        return mark_safe(markdown(self.body, safe_mode='escape'))
    

class ArticleCommentModerator(XtdCommentModerator):
    email_notification = True 
    auto_moderate_field  = 'date_added' 
    moderate_after = 365
    removal_suggestion_notification = True

moderator.register(Article, ArticleCommentModerator)






