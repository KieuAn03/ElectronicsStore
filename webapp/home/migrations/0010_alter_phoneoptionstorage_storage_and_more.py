# Generated by Django 4.2.1 on 2023-06-26 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_coupon'),
        ('home', '0009_phoneoptioncolor_phoneoptionram_phoneoptionstorage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneoptionstorage',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.phonestorage'),
        ),
        migrations.AlterField(
            model_name='tabletoptionram',
            name='ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletram'),
        ),
        migrations.AlterField(
            model_name='tabletoptionstorage',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletstorage'),
        ),
    ]
