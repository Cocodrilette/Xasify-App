from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^sales$', views.sales, name='sales'),
    re_path(r'^inventory$', views.inventory, name='inventory'),
    re_path(r'^add_sell$', views.add_sell, name='add_sell'),
]