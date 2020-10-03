from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.views import get_user_model

from taggit.models  import Tag

from articles.models import Article, Category


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(title="python")
        self.user = get_user_model().objects.create_user(
            username="ademola", email="ademola@gmail.com", password="secret"
        )
        self.article = Article.objects.create(
            author=self.user,
            title="New article",
            body="Article body",
            category=self.category,
            published='P',
        )
        self.article.tags.add('coding')

    # def tearDown(self):
    #     pass

    def test_article_list_view_status_code(self):
        response = self.client.get("/articles/")
        self.assertEqual(response.status_code, 200)
        
    def test_article_list_view(self):
        response = self.client.get(reverse('articles:article_lists'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New article")
        self.assertEqual(Article.objects.count(), 1)
        self.assertTemplateUsed(response, 'articles/article_lists.html')

    def test_category_list_view(self):
        response = self.client.get(reverse('articles:category_list', args=['python']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "python")
        self.assertEqual(Category.objects.count(), 1)
        self.assertTemplateUsed(response, 'articles/category_list.html')

    def test_article_tags_view(self):
        response = self.client.get(reverse('articles:tags', args=['coding']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New article")
        self.assertTemplateUsed(response, 'tag.html')

    def test_article_detail_view(self):
        response = self.client.get('/article/new-article-1/')
        no_response = self.client.get('/article/new-article-10000/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New article")
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'articles/article_detail.html')

    def test_article_create_view(self):
        self.client.login(email='ademola@gmail.com', password='secret')
        response_get = self.client.get(reverse('articles:article_create'))
        self.assertEqual(response_get.status_code, 200)
        self.assertContains(response_get, 'title')
        self.assertTemplateUsed(response_get, 'articles/article_new.html')
        print(self.article.tags.all())
        data =  {
            'title': 'My title',
            'truncated_content': 'My article truncated content',
            'category': self.category,
            'tags': self.article.tags.all()[0],
            'published': 'P',
            'body': 'My title body',
        }
        response_post = self.client.post(reverse('articles:article_create'), data=data)
        print(response_post.context[1])
        # self.assertEquals(Article.objects.count(), 2)
        # self.assertRedirects(response, reverse('articles:article_detail', args=['new-article', 2]))

#     def test_article_update_view(self):
#         response = self.client.post(reverse('articles:article_update', args=['my-title', 1]), {
#             'title': 'My title updated',
#             'body': 'My article body updated'
#         })
#         self.assertEqual(response, 302)

    def test_article_delete_view(self):
        self.client.login(email='ademola@gmail.com', password='secret')
        response = self.client.delete(
            reverse('articles:article_delete',  args=['new-article', 1])
            )
        self.assertEqual(Article.objects.count(), 0)
        self.assertEqual(response.status_code, 302)

# class CategoryViewTest(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(
#             title = 'category'
#         )

#     def test_category_view_status_code(self):
#         response = self.client.get('/article/category/category/')
#         self.assertEqual(response.status_code, 200)

#     def test_category_view(self):
#         response = self.client.get(reverse('articles:category_list', kwargs={"title": self.category.title}), args='category')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'articles/category_list.html')
#         self.assertContains(response, 'category')
