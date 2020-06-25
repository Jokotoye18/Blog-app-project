from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse

# Create your tests here.

class HomepageTest(SimpleTestCase):
    
    def test_homepage_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_view_by_name(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
