from django import forms
from ordersapp.models import Product
from ordersapp.models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        models = Order
        exclude = ('user', '')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='цена', required=False)
    class Meta:
        models = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
        self.fields['product'] = Product.objects.all().select_related()