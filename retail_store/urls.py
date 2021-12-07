from django.urls import path
from . import views

urlpatterns = [
    path('get/product', views.get_product, name='get_product'),
    path('post/product', views.post_product, name='post_product'),
]