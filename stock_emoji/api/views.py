from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Decathlon_Stores , Decathlon_Products
from .serializers import Decathlon_Products_serializers,Decathlon_Stores_serializers,Decathlon_Stores_serializers_create,Decathlon_Products_serializers_create
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView,ListCreateAPIView
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.


class Store_create_apiview(ListCreateAPIView):
  queryset = Decathlon_Stores.objects.all()
  serializer_class = Decathlon_Stores_serializers_create

class Store_retrieve_update_apiview(RetrieveUpdateAPIView):
  queryset = Decathlon_Stores.objects.all()
  serializer_class = Decathlon_Stores_serializers


class Product_create_apiview(ListCreateAPIView):
  queryset = Decathlon_Products.objects.all()
  serializer_class = Decathlon_Products_serializers_create


# api view to get and put product details for the api 
@api_view(['PUT','GET'])
def Stores_product_api(request,store_id,product_id):
   if request.method == 'PUT':
       stu = Decathlon_Products.objects.get(pk=product_id)
       serializer = Decathlon_Products_serializers(stu, data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Complete Data Updated'})
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   if request.method == 'GET':
      if product_id is not None:
         stu = Decathlon_Products.objects.get(pk=product_id)
         serializer = Decathlon_Products_serializers(stu)
         return Response(serializer.data)

      product_object= Decathlon_Products.objects.filter(AssociatedStores=store_id,ProductID=product_id)
      serializers = Decathlon_Products_serializers(product_object,many=True)
      return Response(serializers.data,status=status.HTTP_200_OK)  
      
@api_view()
def product_api(request,id):  
      product_object= Decathlon_Products.objects.filter(AssociatedStores=id)
      serializers = Decathlon_Products_serializers(product_object,many=True)
      return Response(serializers.data,status=status.HTTP_200_OK) 
  
   

    
