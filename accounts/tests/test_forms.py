from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.forms import CustomUserCreationForm


class SignUpFormTest(TestCase):
    def setUp(self):
        self.valid_data = {
            'username': 'userform',
            'email': 'userform@gmail.com',
            'password': 'jokotoye18',
        }

    # def test_user_creation_form(self):
    #     form = CustomUserCreationForm(data=self.valid_data)
    #     self.assertTrue(form.is_valid())
    #     obj = form.save()
    #     self.assertEqual(obj.username, self.valid_data['username'])