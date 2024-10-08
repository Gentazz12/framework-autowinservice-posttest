# Generated by Django 5.1.1 on 2024-09-23 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autowin', '0003_remove_testimonial_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('no_hp', models.CharField(max_length=15)),
                ('alamat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Servis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_servis', models.CharField(max_length=100)),
                ('tanggal_servis', models.DateField()),
                ('biaya', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pelanggan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autowin.pelanggan')),
            ],
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]
