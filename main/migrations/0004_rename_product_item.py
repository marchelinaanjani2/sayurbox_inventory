# Generated by Django 4.2.5 on 2023-09-22 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]
