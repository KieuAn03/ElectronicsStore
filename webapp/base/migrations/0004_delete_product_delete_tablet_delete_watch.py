# Generated by Django 4.1.9 on 2023-06-14 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cart_item_product'),
        ('base', '0003_remove_discount_product_id_remove_laptop_cpu_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Tablet',
        ),
        migrations.DeleteModel(
            name='watch',
        ),
    ]
