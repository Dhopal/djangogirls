from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product


def get_product(request):
    products = Product.objects.all()
    return render(request, 'retail_store/product_list.html', {'products': products})


def post_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            print("Printing request")
            print(request)
            product = form.save(commit=False)
            product.productName = request.POST['productName']
            product.availableQuantity = request.POST['availableQuantity']
            product.save()
            return redirect('/get/product', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'retail_store/product_add.html', {'form': form})
