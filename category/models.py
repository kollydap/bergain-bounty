from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=245)
    description=models.TextField(blank=True)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    
    def __str__(self):
        return self.name