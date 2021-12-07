from django import forms

from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productName', 'availableQuantity',)


class OrderForm(forms.ModelForm):
    productName = forms.ModelChoiceField(queryset=Product.objects.all(),
                                         to_field_name='productName',
                                         empty_label='select product')

    class Meta:
        model = Order
        fields = ('productName', 'quantity',)
