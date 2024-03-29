from rest_framework import serializers
from product.models import Product, UserProduct


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
