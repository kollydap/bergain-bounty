from django.shortcuts import render
from product.models import Product
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
        serialized_product = ProductSerializer(data=data)
        if serialized_product.is_valid():
            serialized_product.save()
            return JsonResponse(serialized_product.data, status=201)
        return JsonResponse(serialized_product.errors, status=400)
