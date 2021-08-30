from django.conf import settings
from django.test import TestCase
from django.test.client import Client
from authapp.models import ShopUser


class TestUserManagement(TestCase):
    username = 'django2'
    user_password = 'geekbrains'

    def setUp(self):
        self.client = Client()

        self.user = ShopUser.objects.create_user(
            username=self.username,
            email='django2@dj.local',
            password=self.user_password,
        )

    def test_login_user(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertContains(response, 'Пользователь', status_code=200)

        user_data = {
            'username': self.username,
            'password': self.user_password
        }

        response = self.client.post('/login/', data=user_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertContains(response, 'Пользователь', status_code=200)

    def test_register_user(self):
        new_user_data = {
            'username': 'django3',
            'email': 'django@gb.local',
            'password1': self.user_password,
            'password2': self.user_password,
            'age': '33'
        }

        response = self.client.post('/register/', data=new_user_data)
        self.assertEqual(response.status_code, 302)

        new_user = ShopUser.objects.get(username=new_user_data['username'])

        activation_url = f'{settings.DOMAIN_NAME}/verify/{new_user_data["email"]}/{new_user.activation_key}'

        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Пользователь', status_code=200)
