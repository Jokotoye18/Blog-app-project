from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from articles.models import Article

class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Article.objects.filter(published='P')

    def lastmod(self, obj):
        return obj.updated_date


class StaticViewSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5
    protocol = 'https'

    def items(self):
        return ['pages:home', 'pages:about', 'pages:contact']

    def location(self, item):
        return reverse(item)