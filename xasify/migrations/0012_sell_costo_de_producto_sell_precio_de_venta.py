# Generated by Django 4.0.4 on 2022-05-15 22:17

from django.db import migrations, models
import xasify.models


class Migration(migrations.Migration):

    dependencies = [
        ('xasify', '0011_delete_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='costo_de_producto',
            field=models.IntegerField(default=0, help_text='Costo de producción del producto', verbose_name=xasify.models.Product),
        ),
        migrations.AddField(
            model_name='sell',
            name='precio_de_venta',
            field=models.IntegerField(default=0, help_text='Precio de venta del producto', verbose_name=xasify.models.Product),
        ),
    ]
