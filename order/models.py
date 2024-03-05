from django.db import models
from product.models import Product,ProductImage
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, null=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)
    paymentMethod = models.CharField(max_length=255, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)

    def __str__(self) -> str:
        return f'{str(self.createdAt)} at {"Deleted User" if self.user == None else self.user.username}'


        
    class Meta:
        ordering = ('-createdAt',)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    productName = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')

    def __str__(self) -> str:
        return f'Order #{self.order.id} - {self.productName}'