from django.shortcuts import render, redirect

from .forms import ProductForm, OrderForm
from .models import Product

from django.contrib.auth.decorators import login_required


def get_product(request):
    products = Product.objects.all()
    return render(request, 'retail_store/product_list.html', {'products': products})


@login_required
def post_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.productName = request.POST['productName']
            product.availableQuantity = request.POST['availableQuantity']
            product.save()
            return redirect('/get/product', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'retail_store/product_add.html', {'form': form})


@login_required
def order_product(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST['quantity']
            productId = request.POST['productId']
            product = Product.objects.get(productId=productId)
            availableQuantity = product.availableQuantity

            print("q=" + quantity + " pid = " + productId + " avl = " + availableQuantity)
            if quantity > availableQuantity:
                form = OrderForm()
                return render(request, 'retail_store/Order_add.html', {'form': form})

            order = form.save(commit=False)
            order.productId = request.POST['productId']
            order.quantity = request.POST['quantity']
            order.customerId = request.user.id
            order.save()
            product.availableQuantity = availableQuantity - quantity
            product.save()
            return redirect('/get/product', pk=product.pk)
    else:
        form = OrderForm()
    return render(request, 'retail_store/Order_add.html', {'form': form})
