# Generated by Django 4.1.2 on 2022-10-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_inventory_quantity_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
