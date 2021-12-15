from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(orderer=user).prefetch_related('product_amount__product')

    def list(self, request, *args, **kwargs):
        order_list = self.get_queryset()
        serialized_data = self.get_serializer(order_list, many=True)
        return Response(serialized_data.data)


# class OrderProductListView(ListAPIView):
#     serializer_class = OrderProductSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         # Book.objects.select_related('publisher').all()
#         return OrderProduct.objects.filter(order__orderer=user).select_related('product')
#
#     def list(self, request, *args, **kwargs):
#         order_product_list = self.get_queryset()
#         serialized_data = self.get_serializer(order_product_list, many=True)
#         return Response(serialized_data.data)
