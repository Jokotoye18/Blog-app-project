from django.contrib import admin
from django.db import models
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Article, ArticleAdmin)

admin.site.register(Category)






