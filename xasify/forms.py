from django.forms import forms
from .models import *
import datetime

class SaleForm(forms.Form):
    
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    seller = forms.ModelChoiceField(queryset=User.objects.all())
    dataTime = forms.DateTimeField(widget=forms.HiddenInput())
    
    def clean_dataTime(self):
        dataTime = self.cleaned_data['dataTime']
        if dataTime > datetime.datetime.now():
            raise forms.ValidationError("Fecha de venta no puede ser mayor a la actual")
        return dataTime
    
    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        seller = cleaned_data.get('seller')
        dataTime = cleaned_data.get('dataTime')
        if not product:
            raise forms.ValidationError("Debe seleccionar un producto")
        if not seller:
            raise forms.ValidationError("Debe seleccionar un vendedor")
        if not dataTime:
            raise forms.ValidationError("Debe seleccionar una fecha")
        if Sales.objects.filter(product=product, seller=seller, dataTime=dataTime).exists():
            raise forms.ValidationError("Ya existe una venta para este producto con este vendedor en esta fecha")
        return cleaned_data
