from django.test import SimpleTestCase
from django.urls import resolve, reverse
from articles.views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView, 
    ArticleUpdateView, 
    ArticleDeleteView, 
    CategoryListView, 
    SearchView,
    ArticleTagView,
    markdown_uploader,
) 

class TestUrls(SimpleTestCase):
    def test_article_list_resolve(self):
        url = reverse('articles:article_lists')
        self.assertEqual(resolve(url).func.view_class, ArticleListView)
    
    def test_article_detail_resolve(self):
        url = reverse('articles:article_detail', args=['some-slug', '1'])
        self.assertEqual(resolve(url).func.view_class, ArticleDetailView)

    def test_article_update_resolve(self):
        url = reverse('articles:article_update', args=['some-slug', '1'])
        self.assertEqual(resolve(url).func.view_class, ArticleUpdateView)

    def test_article_delete_resolve(self):
        url = reverse('articles:article_delete', args=['some-slug', '1'])
        self.assertEqual(resolve(url).func.view_class, ArticleDeleteView)

    def test_article_create_resolve(self):
        url = reverse('articles:article_create')
        self.assertEqual(resolve(url).func.view_class, ArticleCreateView)

    def test_category_list_resolve(self):
        url = reverse('articles:category_list', args=['python'])
        self.assertEqual(resolve(url).func.view_class, CategoryListView)

    def test_article_tag_resolve(self):
        url = reverse('articles:tags', args=['category-slug'])
        self.assertEqual(resolve(url).func.view_class, ArticleTagView)

    def test_article_search_resolve(self):
        url = reverse('articles:search')
        self.assertEqual(resolve(url).func.view_class, SearchView)

    def test_api_upload_resolve(self):
        url = reverse('articles:markdown_uploader_page')
        self.assertEqual(resolve(url).func, markdown_uploader)