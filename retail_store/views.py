import uuid

from django.shortcuts import render, redirect

from .forms import ProductForm
from .forms import OrderForm
from .models import Product

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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
            productName = request.POST['productName']

            print(productName)

            product = Product.objects.get(productName=productName)
            availableQuantity = product.availableQuantity

            print("q=" + str(quantity) + " pn = " + productName + " avl = " + str(availableQuantity))
            if int(quantity) > availableQuantity:
                form = OrderForm()
                return render(request, 'retail_store/Order_add.html', {'form': form})

            order = form.save(commit=False)
            order.productName = product
            order.quantity = quantity
            print("print user id")
            print(request.user.id)
            user = User.objects.get(id=request.user.id)
            order.customerId = user

            order.save()
            product.availableQuantity = int(availableQuantity) - int(quantity)
            product.save()
            return redirect('/get/product', pk=product.pk)
    else:
        form = OrderForm()
    return render(request, 'retail_store/Order_add.html', {'form': form})
