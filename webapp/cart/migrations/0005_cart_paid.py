# Generated by Django 4.1.9 on 2023-07-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_historycart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
