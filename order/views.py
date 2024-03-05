from django.shortcuts import render
from .models import Order,OrderItem
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import OrderViewSerializer,OrderItemSerializer

#this is just like the LISTCREATEAPIVIEW
class OrderView(APIView):
    def get(self, request):
        orders=Order.objects.all()
        serializer=OrderViewSerializer(orders,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=OrderViewSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetailView(APIView):
    def get(self,request,pk):
        orders=Order.objects.get(pk=pk)
        serializer=OrderViewSerializer(orders,many=False)
        return Response(serializer.data)
    
    def put(self,request,pk):
        orders=Order.objects.get(pk=pk)
        serializer=OrderViewSerializer(orders,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, pk):
        orders=Order.objects.get(pk=pk)
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class OrderItemView(APIView):
    def post(self,request):
        serializer=OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
