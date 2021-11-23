from rest_framework import serializers

from order.models import Order, OrderProduct


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['orderer', 'date_of_order', 'address', 'date_of_delivery']


class OrderProductSerializer(serializers.ModelSerializer):
    # todo queryset - The queryset used for model instance lookups when validating the field input. Relationships must either set a queryset explicitly, or set read_only=True.
    product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['order', 'product', 'amount']
