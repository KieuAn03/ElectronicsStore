# Generated by Django 4.1.9 on 2023-06-25 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_delete_product_delete_tablet_delete_watch'),
        ('home', '0007_alter_phoneoption_color_alter_phoneoption_ram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabletOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('Phone_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tablet')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletcolor')),
                ('ram', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletram')),
                ('storage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletstorage')),
            ],
        ),
    ]
