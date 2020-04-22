from django.db import models
from django.conf import settings 
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator, XtdCommentModerator

#from django_comments.moderation import CommentModerator
#from django_comments_xtd.moderation import moderator, XtdCommentModerator


ARTICLE_CATEGORIES = [
    ('Django', 'django'),
    ('Python', 'python'),
    ('Other', 'other')
]
class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=30, choices=ARTICLE_CATEGORIES)
    body = models.TextField()
    slug = models.SlugField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    objects = models.Manager() 

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[self.slug, (self.pk)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class ArticleCommentModerator(XtdCommentModerator):
    email_notification = True 
    auto_moderate_field  = 'date_added' 
    moderate_after = 365
    removal_suggestion_notification = True

moderator.register(Article, ArticleCommentModerator)


