# Generated by Django 4.0.4 on 2022-05-14 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xasify', '0004_sell_datatime_sell_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='utility',
            field=models.IntegerField(default=0, help_text='Utilidad del producto'),
            preserve_default=False,
        ),
    ]
