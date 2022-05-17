from itertools import product
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from xasify.models import *
from django.db.models import Sum


@login_required
def index(request):
    return render(
        request, 
        'index.html',)

@login_required
def sales(request):
    sales = Sales.objects.order_by("-dataTime")
    price = Sales.objects.all().aggregate(Sum('product__price'))
    return render(
        request, 
        'sales.html',
        context={
            'sales': sales,
            'price': price,
            })

@login_required
def inventory(request):
    products = Product.objects.order_by("name")
    return render(
        request, 
        'inventory.html',
        context={
            'products': products,
            })

@login_required
def sell(request):
    user = User.username
    products = Product.objects.order_by("name")
    return render(
        request, 
        'sell.html',
        context={
            'products': products,
            'user': user,
            })

from django.contrib import messages

@login_required
def add_sell(request):
    products = Product.objects.order_by("name")
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sale was successfully😎')
            return render(
                request, 
                'add_sell.html',
                context={
                    'form': form,
                    'products': products,
                    })
    else:
        form = SaleForm()
    return render(
        request, 
        'add_sell.html',
        context={
            'form': form,
            'products': products,
            })