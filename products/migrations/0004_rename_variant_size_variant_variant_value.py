# Generated by Django 5.1.3 on 2024-11-16 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_variant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variant',
            old_name='variant_size',
            new_name='variant_value',
        ),
    ]
