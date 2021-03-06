from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.
class AccountViewsTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'newuser',
            email = 'newuser@gmail.com',
            password = 'secret',
        )

    def test_model_content(self):
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'newuser' )
        self.assertEqual(get_user_model().objects.all()[0].email, 'newuser@gmail.com' )



# class AccountUpdateView(TestCase):

#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username = 'ademola',
#             email = 'ademola@gmail.com'
#         )
#     def test_accounts_update_status_code(self):
#         response = self.client.get('/accounts/')
#         self.assertEqual(response.status_code, 200)

#     def test_account_update_view_by_name(self):
#         response = self.client.get(reverse('accounts:account_update'))
#         self.assertEqual(response.status_code, 200)

#     def test_account_update_view_uses_correct_template(self):
#         response = self.client.get(reverse('accounts:account_update'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'accounts/account_update.html')

#     def test_account_update_view(self):
#         response = self.client.post(reverse('accounts:account_update'),{
            
#         })
#         user_update = self.user
#         response = self.client.post(reverse('accounts:account_update'), {'user_updated':user_update})
#         self.assertEqual(response.status_code, 302)
        

