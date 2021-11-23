from django.db import models

from core.models import User
from catalog.models import Product


class Order(models.Model):
    orderer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_order = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)
    address = models.CharField(max_length=200)
    date_of_delivery = models.DateTimeField()

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

    status = models.CharField(choices=STATUSES_CHOICES, max_length=12)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
