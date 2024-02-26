from django.shortcuts import render
from product.models import Product
from cart.models import CartItem, Cart
from django.contrib.auth.models import User
from cart.serializers import CartItemSerializer, CartSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# todo use try block
@csrf_exempt
def index(request):
    if request.method == "GET":
        cart = Cart.objects.all()
        serialized_cart = CartSerializer(instance=cart, many=True)
        return JsonResponse(data=serialized_cart.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serialized_cart = CartSerializer(data=data)
        if serialized_cart.is_valid():
            serialized_cart.save()
            return JsonResponse(serialized_cart.data, status=201)
        return JsonResponse(serialized_cart.errors, status=400)


@csrf_exempt
def create_cart_item(request):
    """
    To  add to cart
    """
    if request.method == "POST":
        data = JSONParser().parse(request)
        serialized_cart_item = CartItemSerializer(data=data)
        if serialized_cart_item.is_valid():
            user_id = data.get("user_id")
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)

            cart, created = Cart.objects.get_or_create(user=user)
            serialized_cart_item.save(cart=cart)

            return JsonResponse(serialized_cart_item.data, status=201)
        return JsonResponse(serialized_cart_item.errors, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
