from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_images/",  null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sellers")
    is_sold=models.BooleanField(default=False)
    
    # Add other fields as needed (e.g., category, condition)

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField(max_length=300)
# class UserProduct(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Add fields like listing date, status, etc.
    
