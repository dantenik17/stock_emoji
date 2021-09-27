from django.contrib import admin

# Register your models here.
from .models import Decathlon_Products,Decathlon_Stores

@admin.register(Decathlon_Stores)
class Decathlon_Stores_Admin(admin.ModelAdmin):
    list_display=['StoreID','StoreName','StoreCity']

#@admin.register(Decathlon_Products)
#class Decathlon_Products_Admin(admin.ModelAdmin):
#    list_display=['ProductID','ProductName','ProductSport','ProductLevel','ProductDescription','AssociatedStores']
admin.site.register(Decathlon_Products)