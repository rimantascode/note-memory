from django.contrib import admin

from .models import Product, OrderSummary

admin.site.register(Product)
admin.site.register(OrderSummary)

