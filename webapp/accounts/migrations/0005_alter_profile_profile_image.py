# Generated by Django 4.2.1 on 2023-07-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_profile_password_remove_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='profile_images'),
        ),
    ]
