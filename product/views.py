from django.shortcuts import render
from product.models import Product
from django.contrib.auth.models import User
from product.serializers import ProductSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# todo use try block
@csrf_exempt
def index(request):
    if request.method == "GET":
        product = Product.objects.all()
        serialized_product = ProductSerializer(instance=product, many=True)
        return JsonResponse(data=serialized_product.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        print(data)
        serialized_product = ProductSerializer(data=data)
        if serialized_product.is_valid():
            serialized_product.save()
            print(serialized_product)
            return JsonResponse(serialized_product.data, status=201)
        return JsonResponse(serialized_product.errors, status=400)


@csrf_exempt
def product_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        product_serializer = ProductSerializer(product)
        return JsonResponse(product_serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        product.delete()
        return HttpResponse(status=204)


@csrf_exempt
def getsellerproduct(request, user_id):
    try:
        seller = User.objects.get(pk=user_id)
        product = Product.objects.filter(seller=seller)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serialized_product = ProductSerializer(instance=product, many=True)
        return JsonResponse(data=serialized_product.data, safe=False)


