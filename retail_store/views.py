from django.shortcuts import render
from .models import Product


def get_products(request):
    products = Product.objects.all()
    return render(request, 'retail_store/product_list.html', {'products': products})
