from django.core.management import call_command
from django.test import TestCase
from django.test.client import Client

from mainapp.models import ProductCategory, Product


class MainAppSmoletest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_list(self):
        for product_item in Product.objects.all():
            response = self.client.get(f'/products/product/{product_item.pk}')
            self.assertEqual(response.status_code, self.status_code_success)

    def test_categories_list(self):
        for category_item in Product.objects.all():
            response = self.client.get(f'/products/category/{category_item.pk}')
            self.assertEqual(response.status_code, self.status_code_success)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')

class ProductsTestCase(TestCase):
   def setUp(self):
       category = ProductCategory.objects.create(name="стулья")
       self.product_1 = Product.objects.create(name="стул 1", category=category, price=1999.5, quantity=150)

   def test_product_get(self):
       product_1 = Product.objects.get(name="стул 1")
       self.assertEqual(product_1, self.product_1)

   def test_product_print(self):
       product_1 = Product.objects.get(name="стул 1")
       self.assertEqual(str(product_1), 'стул 1 (стулья)')

