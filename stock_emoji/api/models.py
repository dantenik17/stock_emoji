from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField

# Create your models here.
class Decathlon_Stores(models.Model):
    StoreID  = models.IntegerField(primary_key=True)
    StoreName  = models.CharField(max_length=100)
    StoreCity  = models.CharField(max_length=100)
     
    def __str__(self):
       return self.StoreName 

class Decathlon_Products(models.Model):
    ProductID  = models.IntegerField(primary_key=True)
    ProductName  = models.CharField(max_length=100)
    ProductSport =models.CharField(max_length=100)
    ProductLevel =models.CharField(max_length=100)
    ProductDescription  = models.TextField()
    #AssociatedStores = ForeignKey(Decathlon_Stores,on_delete=models.CASCADE)
    AssociatedStores = ManyToManyField(Decathlon_Stores)
    
    def __str__(self):
        return self.ProductName  