from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(verbose_name="Производитель", max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Type(models.Model):
    name = models.CharField(verbose_name="Тип товара", max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название", blank=False, null=False)
    description = models.CharField(max_length=1000, verbose_name="Название")
    price = models.CharField(max_length=6, verbose_name="Цена")
    seller = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    in_stock = models.IntegerField(verbose_name="В наличии")
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
