from rest_framework import serializers

from order.models import Order, ProductAmount
from catalog.serializers import ProductSerializer


class ProductAmountSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = ProductAmount
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    product_amount = ProductAmountSerializer(many=True)

    class Meta:
        model = Order
        fields = ['date_of_order', 'address', 'date_of_delivery', 'product_amount']

