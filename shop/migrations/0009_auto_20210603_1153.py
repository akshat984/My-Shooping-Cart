# Generated by Django 3.1.5 on 2021-06-03 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='amount',
        ),
    ]
