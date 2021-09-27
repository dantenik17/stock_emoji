"""stock_emoji URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register('stores', views.Stores_viewset, basename='stores')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include(router.urls)),
    path('stores/', views.Store_create_apiview.as_view()),
    path('stores/<int:pk>/', views.Store_retrieve_update_apiview.as_view()),
    path('products/', views.Product_create_apiview.as_view()),
    path('stores/<int:id>/products/',views.product_api),
    path('stores/<int:store_id>/products/<int:product_id>',views.Stores_product_api),
    
]
