from django.contrib import admin
from order.models import Order, ProductAmount

admin.site.register(Order)
admin.site.register(ProductAmount)
