from django.shortcuts import render
from product.models import Product
from cart.models import CartItem, Cart
from django.contrib.auth.models import User
from cart.serializers import CartItemSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
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


@csrf_exempt
def get_user_cart(request, pk):
    if request.method == "GET":
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        
        cart, cart_created = Cart.objects.get_or_create(user=user)
        serialized_cart = CartSerializer(instance=cart)
        
        return JsonResponse(data=serialized_cart.data, status=200)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


# class CartView(APIView):
#     def get(self, request):
#         cart=Cart.objects.get_or_create(user=request.user)[0]
#         serializer=CartSerializer(cart)
#         return Response(serializer.data)
    

# class CartAddView(APIView):
#     def post(self, request):
#         if not request.user.is_authenticated:
#             return Response({"error": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
#         product=request.data.get("product")
#         quantity=request.data.get("qunatity")
#         cart=Cart.objects.get_or_create(user=request.user)[0]
#         cart_item, created=CartItem.objects.get_or_create(cart=cart, product=product)
#         if not created:
#             cart_item.quantity+=int(quantity)
#             cart_item.save()
#             serializer=CartItemSerializer(cart)
#             return Response(serializer.data)
    
# class CartRemoveView(APIView):
#     def post(self, request):
#         product_id=request.data.get("product_id")
#         cart=Cart.objects.get(user=request.user)
#         cart_item=CartItem.objects.get(cart=cart, product_id=product_id)
#         cart_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)