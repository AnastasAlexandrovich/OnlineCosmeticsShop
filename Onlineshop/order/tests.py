import mock
from django.test import TestCase
from django_mock_queries.query import MockSet, MockModel

from .models import Order


class OrderListViewTest(TestCase):
    qs = MockSet(
        MockModel(id=1, orderer=1, date_of_order="01.02.2022", address="Some street",
                  date_of_delivery="02.02.2022", product_amount="1", status='Новый'))

    @mock.patch('order.models.Order.objects.all', qs)
    def test_some_function(self):
        orders = Order.objects.all
        self.assertEqual(len(orders), 1)






