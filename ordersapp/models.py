from django.conf import settings
from django.db import models

from mainapp.models import Product

class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    DELIVERY = 'DLV'
    DONE = 'DN'
    CANCELED = 'CNC'

    STATUSES = (
        (FORMING, 'формирование'),
        (SENT_TO_PROCEED, 'передан в обработку'),
        (DELIVERY, 'передан курьеру'),
        (DONE, 'выдан'),
        (CANCELED, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, default=FORMING, max_length=3)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ номер {self.pk}'

    def get_product_type_quantity(self):
        items = self.orderitems.select_related()
        return len(items)

    def get_total_quantity(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_total_cost(self):
        items = self.orderitems.select_related()
        return sum(list(map(lambda x: x.quantity * x.product.price, items)))

    def get_summary(self):
        items = self.orderitems.select_related()
        return {
            'total_quantity': sum(list(map(lambda x: x.quantity, items))),
            'toal_cost': sum(list(map(lambda x: x.quantity * x.product.price, items)))
        }

    def delete(self):
        for item in self.orderitems.select_related():
            item.product.quantity += item.quantity
            item.product.save()

        self.is_active = False
        self.save()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderitems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,  verbose_name='продукты', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='количесто', default=0)

    @property
    def get_product_cost(self):
        return self.quantity * self.product.price

    @staticmethod
    def get_product(user, product):
        return OrderItem.objects.filter(user=user, product=product)