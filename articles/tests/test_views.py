# from django.test import TestCase,Client
# from  articles.models import  Article, Category
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# # Create your tests here.

# class ArticleViewTest(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(
#             title = 'test category'
#         )
#         self.user = get_user_model().objects.create_user(
#             username = 'ademola',
#             email = 'ademola@gmail.com',
#             password = 'secret'
#         )

#         self.article = Article.objects.create(
#             author = self.user,
#             title = 'New article',
#             body = 'Article body',
#             category = self.category,
#             tags = 'test tag'
#         )

#     def test_article_list_view_status_code(self):
#         response = self.client.get('/articles/')
#         self.assertEqual(response.status_code, 200)

#     def test_article_list_view(self):
#         response = self.client.get(reverse('articles:article_lists'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'New article')
#         self.assertTemplateUsed(response, 'articles/article_lists.html')

#     def test_article_detail_view(self):
#         response = self.client.get('/article/1/')
#         no_response = self.client.get('/article/10000/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'New article')
#         self.assertContains(response, 'Article body')
#         self.assertContains(response, 'ademola')
#         self.assertContains(response, 'test category')
#         self.assertContains(response, 'test python')
#         self.assertTemplateUsed(response, 'articles/article_detail.html')

#     def test_article_create_view(self):
#         response = self.client.post(reverse('articles:article_create'), {
#             'title': 'My title',
#             'body': 'My title body',
#             'author': self.user,
#             'category': 'test category1',
#             'tags': 'test tag1',
#         })
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'My title')
#         self.assertContains(response, 'My title body')

#     def test_article_update_view(self):
#         response = self.client.post(reverse('articles:article_update', args=['my-title', 1]), {
#             'title': 'My title updated',
#             'body': 'My article body updated'
#         })
#         self.assertEqual(response, 302)

#     def test_article_delete_view(self):
#         response = self.client.get(
#             reverse('articles:article_delete',  args=['my-title', 1])
#             )
#         self.assertEqual(response.status_code, 200)


# class CategoryViewTest(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(
#             title = 'category'
#         )

#     def test_category_view_status_code(self):
#         response = self.client.get('/article/category/category/')
#         self.assertEqual(response.status_code, 200)

#     def test_category_view(self):
#         response = self.client.get(reverse('articles:category_list'), args='category')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'articles/category_list.html')
#         self.assertContains(response, 'category')
