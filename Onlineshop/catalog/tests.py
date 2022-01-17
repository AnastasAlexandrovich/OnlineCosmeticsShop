import tempfile

import pytest
from django.test import TestCase
from pytest_postgresql import factories

from .models import Product, Manufacturer, Type


class ProductListViewTest(TestCase):

    def setUp(self):
        a = Manufacturer.objects.create(name="Loreal")
        t = Type.objects.create(name="vvvv")
        Product.objects.create(name="FRFR", description="d", price=10, seller=a, in_stock=1, type=t)

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""

