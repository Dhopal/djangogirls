from django.db import models
import uuid
from django.conf import settings


class Product(models.Model):
    productName = models.CharField(max_length=200, null=True, unique=True)
    productId = models.UUIDField(default=uuid.uuid4, editable=True, null=True)
    availableQuantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.productName


class Order(models.Model):
    orderId = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)
    customerId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    productName = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.orderId)
