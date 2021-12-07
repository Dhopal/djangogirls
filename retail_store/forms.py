from django import forms

from .models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('productName', 'availableQuantity',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('productId', 'quantity',)