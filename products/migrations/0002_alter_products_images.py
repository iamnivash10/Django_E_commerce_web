# Generated by Django 5.1.3 on 2024-11-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='photos/products/'),
        ),
    ]