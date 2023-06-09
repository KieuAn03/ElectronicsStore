# Generated by Django 4.1.9 on 2023-06-14 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='voucher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='producttype',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='discount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discount', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.product')),
            ],
        ),
    ]
