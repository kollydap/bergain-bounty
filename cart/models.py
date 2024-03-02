from django.db import models
from django.contrib.auth.models import User
from product.models import Product
import uuid

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartItem")

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name