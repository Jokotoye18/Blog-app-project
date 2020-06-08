from django.apps import AppConfig

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

class ArticlesConfig(AppConfig):
    name = 'articles'
