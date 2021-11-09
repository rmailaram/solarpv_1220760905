from django.shortcuts import render
from rest_framework import generics
from .models import Product, Certificate, Service
from .api.serializers import Serializers

# Create your views here.
class views:
    class ProductListView(generics.ListAPIView): 
        queryset = Product.objects.all() 
        serializer_class = Serializers.ProductSerializer

    class ProductDetailView(generics.RetrieveAPIView): 
        queryset = Product.objects.all() 
        serializer_class = Serializers.ProductSerializer


    class CertificateListView(generics.ListAPIView): 
        queryset = Certificate.objects.all() 
        serializer_class = Serializers.CertificateSerializer

    class CertificateDetailView(generics.RetrieveAPIView): 
        queryset = Certificate.objects.all() 
        serializer_class = Serializers.CertificateSerializer
        

    class ServiceListView(generics.ListAPIView): 
        queryset = Service.objects.all() 
        serializer_class = Serializers.ServiceSerializer

    class ServiceDetailView(generics.RetrieveAPIView): 
        queryset = Service.objects.all() 
        serializer_class = Serializers.ServiceSerializer

