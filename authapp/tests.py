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
        self.assertNotContains(response, 'Пользователь', status_code=200)

        user_data = {
            'username': self.username,
            'password': self.user_password
        }

        response = self.client.post('/auth/login/', data=user_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertNotContains(response, 'Пользователь', status_code=200)


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

    def test_basket_login_redirect(self):
           # без логина должен переадресовать
           response = self.client.get('/basket/')
           self.assertEqual(response.url, '/?next=/basket/')
           self.assertEqual(response.status_code, 302)

           # с логином все должно быть хорошо
           self.client.login(username=self.username, password=self.user_password)

           response = self.client.get('/basket/')
           self.assertEqual(response.status_code, 200)
           self.assertEqual(list(response.context['basket']), [])
           self.assertEqual(response.request['PATH_INFO'], '/basket/')
           self.assertIn('Ваша корзина, Пользователь', response.content.decode())
