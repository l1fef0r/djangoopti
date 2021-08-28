from django.db import models
from django.conf import settings
from django.utils.functional import cached_property

from mainapp.models import Product

class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    
    def get_product_cost(self):
        return self.product.price * self.quantity
    
    product_cost = property(get_product_cost)

    @cached_property
    def get_items_cashed(self):
#        return self.user.basket.select_related()
        return Basket.objects.filter(user=self.user)

    def get_total_quantity(self):
#        _items = Basket.objects.filter(user=self.user)
        _items = self.get_items_cashed
        return sum(list(map(lambda x: x.quantity, _items)))

    def get_total_cost(self):
#        _items = Basket.objects.filter(user=self.user)
        _items = self.get_items_cashed
        return sum(list(map(lambda x: x.product_cost, _items)))

    @staticmethod
    def get_product(user, product):
        return Basket.objects.filter(user=user, product=product)

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user)
#        return user.basket.select_related()

    @classmethod
    def get_products_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]

        return basket_items_dic

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()

    def save(self, *args, **kwargs):
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)
