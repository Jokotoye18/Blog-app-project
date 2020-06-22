from django.contrib import admin
from django.db import models
from .models import Article, Category
from markdownx.widgets import AdminMarkdownxWidget

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
admin.site.register(Article, ArticleAdmin)

admin.site.register(Category)






