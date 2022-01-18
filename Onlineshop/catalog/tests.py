from django.test import TestCase

from .models import Product, Manufacturer, Type


class ProductListViewTest(TestCase):

    def setUp(self):
        a = Manufacturer.objects.create(name="Loreal")
        t = Type.objects.create(name="Помада")
        Product.objects.create(name="супер помада 1", description="1", price=10, seller=a, in_stock=1, type=t)
        Product.objects.create(name="супер помада 2", description="2", price=10, seller=a, in_stock=3, type=t)
        Product.objects.create(name="супер помада 3", description="3", price=10, seller=a, in_stock=5, type=t)

    def test_animals_can_speak(self):
        resp = self.client.get('/products/')
        self.assertEqual(resp.status_code, 200)
        product_list = resp.json()
        self.assertEqual(len(product_list), 3)
        pass

