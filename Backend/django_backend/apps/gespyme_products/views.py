from django.shortcuts import render
# Generic views import
from rest_framework import generics
from apps.gespyme_products.models import Product
from apps.gespyme_products.serializers import ProductSerializer


# Product List view
class list_products(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product Retrieve data view
class retrieve_product(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product Create view
class create_product(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Product Update View
class update_product(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# Product Delete view
class destoy_product(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
