from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from catalog.serializers import ProductSerializer
from catalog.models import Product


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class SingleProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
