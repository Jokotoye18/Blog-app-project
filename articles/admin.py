from django.contrib import admin
from .models import Article, Category
from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

admin.site.register(Article, ArticleAdmin)

admin.site.register(Category)






