from rest_framework import serializers
from cart.models import CartItem, Cart


# Serializers define the API representation.
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    # Define a custom field for user_id
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ["product", "quantity", "user_id"]

    def create(self, validated_data):
        # Pop the user_id from validated_data
        user_id = validated_data.pop("user_id")

        # Fetch or create the cart associated with the user
        cart, created = Cart.objects.get_or_create(user=user_id)

        # Create the cart item and associate it with the cart
        cart_item = CartItem.objects.create(**validated_data)

        return cart_item
