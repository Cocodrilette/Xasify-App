
from django.db import models
from django.contrib.auth.models import User
import datetime

# wild_books = Book.objects.filter(title__contains='wild')
# number_wild_books = Book.objects.filter(title__contains='wild').count()

class Product(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField(help_text='Costo del producto')
    price = models.IntegerField(help_text='Precio de ventana del producto')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Sales(models.Model):  
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # blank=True para que no sea requerido
    dataTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["dataTime"]

    def __str__(self):
        return self.product.name

from django.forms import ModelForm

class SaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['product', 'seller',]

