# Generated by Django 4.0.4 on 2022-05-14 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xasify', '0006_remove_product_utility'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sell',
            options={'ordering': ['-dataTime'], 'verbose_name_plural': 'Sales'},
        ),
    ]
