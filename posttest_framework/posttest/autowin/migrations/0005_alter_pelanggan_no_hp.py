# Generated by Django 5.1.1 on 2024-09-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autowin', '0004_pelanggan_servis_delete_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelanggan',
            name='no_hp',
            field=models.CharField(max_length=20),
        ),
    ]
