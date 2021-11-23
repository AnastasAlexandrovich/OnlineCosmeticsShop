from django.shortcuts import render
from rest_framework.generics import ListAPIView

from catalog.serializers import ProductSerializer
from catalog.models import Product


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
