from django.db import models

from core.models import User
from catalog.models import Product


class ProductAmount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Продукт - Количество'


class Order(models.Model):
    orderer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_order = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True)
    address = models.CharField(verbose_name='Адрес доставки', max_length=200, null=True, blank=True)
    date_of_delivery = models.DateTimeField(verbose_name='Дата доставки')
    product_amount = models.ManyToManyField(ProductAmount)

    NEW = 'NEW'
    PAID = 'PAID'
    DELIVERING = 'DELIVERING'
    DELIVERED = 'DELIVERED'

    STATUSES_CHOICES = [
        (NEW, 'Новый'),
        (PAID, 'Оплачен'),
        (DELIVERING, 'В доставке'),
        (DELIVERED, 'Доставлен')
    ]

    status = models.CharField(verbose_name='Статус заказа', choices=STATUSES_CHOICES, max_length=12)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    # def get_product(self):
    #     pr = ProductAmount.objects.all()
    #     return pr
