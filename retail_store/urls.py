from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='get_products'),
]