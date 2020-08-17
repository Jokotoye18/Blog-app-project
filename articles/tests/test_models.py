from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from taggit.models import Tag

from  articles.models import  Article, Category


class TestArticleModels(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            title = 'category test'
        )

        self.user = get_user_model().objects.create_user(
            username = 'ademola',
            email = 'ademola@gmail.com',
            password = 'secret'
        )

        self.article = Article.objects.create(
            author = self.user,
            title = 'New article',
            body = 'Article body',
            category = self.category,
        )
        self.article.tags.add('coding', 'programming')

    def test_string_represention(self):
        self.assertEqual(str(self.article), 'New article')

    def test_get_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), '/article/new-article-1/')

    def test_article_content(self):
        self.assertEqual(f'{self.article.author.username}', 'ademola')
        self.assertEqual(f'{self.article.title}', 'New article')
        self.assertEqual(f'{self.article.body}', 'Article body')
        self.assertEqual(f'{self.article.category.title}', 'category test')
        self.assertEqual(f'{self.article.slug}', 'new-article')
        



class CategoryModelViewTest(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(
            title = 'Test category',
        )

    def test_string_represention(self):
        self.assertEqual(str(self.category), 'Test category')


    def test_article_content(self):
        self.assertEqual(f'{self.category.title}', 'Test category')
