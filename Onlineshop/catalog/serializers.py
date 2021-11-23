from rest_framework import serializers
from catalog.models import Manufacturer, Type, Product


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['name']


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    type = TypeSerializer()

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'seller', 'in_stock', 'type']
