from django.contrib import admin
from catalog.models import Manufacturer, Type, Product

admin.site.register(Manufacturer)
admin.site.register(Type)
admin.site.register(Product)