from django.db import models
from django.conf import settings 
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator, XtdCommentModerator



class Article(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    objects = models.Manager() 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail', args=[str(self.pk)])


class ArticleCommentModerator(XtdCommentModerator):
    email_notification = True 
    auto_moderate_field  = 'date_added' 
    moderate_after = 365
    removal_suggestion_notification = True

moderator.register(Article, ArticleCommentModerator)


