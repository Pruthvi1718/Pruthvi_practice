from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#serializer
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#create home url
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

#add product
from django.shortcuts import render

def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'home.html', {'products': products})