from django.test import TestCase,Client
from .models import  Article
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class ArticleModelViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'ademola',
            email = 'ademola@gmail.com',
            password = 'secret'
        )

        self.article = Article.objects.create(
            author = self.user,
            title = 'New article',
            body = 'Article body'
        )

    def test_string_represention(self):
        self.assertEqual(str(self.article), 'New article')

    def test_get_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), '/article/1/')

    def test_article_content(self):
        self.assertEqual(f'{self.article.author.username}', 'ademola')
        self.assertEqual(f'{self.article.title}', 'New article')
        self.assertEqual(f'{self.article.body}', 'Article body')

    def test_article_list_view(self):
        response = self.client.get(reverse('articles:article_lists'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New article')
        self.assertTemplateUsed(response, 'articles/article_lists.html')

    def test_article_detail_view(self):
        response = self.client.get('/article/1/')
        no_response = self.client.get('/article/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'New article')
        self.assertContains(response, 'Article body')
        self.assertContains(response, 'ademola')
        self.assertTemplateUsed(response, 'articles/article_detail.html')

    def test_article_create_view(self):
        response = self.client.post(reverse('articles:article_create'), {
            'title': 'My title',
            'body': 'My title body',
            'author': self.user
        })
        self.assertEqual(response.status_code, 302)
        self.assertContains(response, 'My title')
        self.assertContains(response, 'My title body')

    def test_article_update_view(self):
        response = self.client.get(reverse('articles:article_update', kwargs={'pk': 1}), {
            'title': 'My title updated',
            'body': 'My article body updated'
        })
        self.assertEqual(response, 200)

    def test_article_delete_view(self):
        response = self.client.get(
            reverse('articles:article_delete', args='1')
            )
        self.assertEqual(response, 200)





