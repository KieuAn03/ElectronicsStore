# Generated by Django 4.1.9 on 2023-07-21 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('home', '0007_alter_phoneoptioncolor_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablet',
            name='BackCamera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletbackcamera'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='Connect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletconnect'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='FrontCamera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletfrontcamera'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletstorage'),
        ),
    ]
