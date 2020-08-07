from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from articles.models import Article


class ArticlesFeed(Feed):
    title = 'Jokotoye Ademola Blog'
    link = ''
    description = 'All articles of my Blog'

    def items(self):
        return Article.objects.filter(published='P')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)