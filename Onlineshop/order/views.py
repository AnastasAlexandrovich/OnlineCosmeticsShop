from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(orderer=user)

    def list(self, request, *args, **kwargs):
        order_list = self.get_queryset()
        serialized_data = self.get_serializer(order_list, many=True)
        return Response(serialized_data.data)
