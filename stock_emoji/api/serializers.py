from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Decathlon_Products,Decathlon_Stores

class Decathlon_Stores_serializers(serializers.ModelSerializer):
    class Meta:
        model=Decathlon_Stores
        fields='__all__'
        #fields=['StoreID','StoreName','StoreCity']
        read_only_fields=['StoreID','StoreName']

class Decathlon_Products_serializers(serializers.ModelSerializer):
    class Meta:
        model=Decathlon_Products
        fields='__all__'
        #fields=['ProductID','ProductName','ProductSport','ProductLevel','ProductDescription','AssociatedStores']
        read_only_fields=['ProductID','ProductName','AssociatedStores']        

class Decathlon_Products_serializers_create(serializers.ModelSerializer):
    class Meta:
        model=Decathlon_Products
        fields='__all__'
        #fields=['ProductID','ProductName','ProductSport','ProductLevel','ProductDescription','AssociatedStores']
        #read_only_fields=['ProductID','ProductName','AssociatedStores']       

class Decathlon_Stores_serializers_create(serializers.ModelSerializer):
    class Meta:
        model=Decathlon_Stores
        fields='__all__'
        #fields=['StoreID','StoreName','StoreCity']
        #read_only_fields=['StoreID','StoreName']        