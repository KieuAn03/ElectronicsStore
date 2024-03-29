# Generated by Django 4.1.9 on 2023-07-21 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('home', '0005_remove_laptop_release_date_alter_laptop_cpu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablet',
            name='Info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='OS',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletos'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='battery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletbattery'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletbrand'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='chips',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletchip'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletcolor'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='image0',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletram'),
        ),
        migrations.AlterField(
            model_name='tablet',
            name='screen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tabletscreen'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='BoMay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.watchbomay'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='Brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.watchbrand'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='ChatLieu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.watchchatlieu'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='ChongNuoc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.watchchongnuoc'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='Day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.watchday'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='DoiTuong',
            field=models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('UniSex', 'Unisex')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='watch',
            name='DuongKinh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.watchdiameter'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='Info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='watch',
            name='QuocGia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.watchquocgia'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='image0',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='watch',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
