# Generated by Django 4.0.4 on 2022-05-14 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xasify', '0007_alter_sell_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='sell',
            options={'ordering': ['-dataTime']},
        ),
    ]
