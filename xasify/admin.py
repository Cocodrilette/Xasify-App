from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'price',)
    list_filter = ['name']
    field = ['name', ('cost', 'price')]

@admin.register(Sales)
class SellAdmin(admin.ModelAdmin):
    list_display = ('product', 'seller', 'dataTime',)
    list_filter = ('product', 'seller', 'dataTime')
