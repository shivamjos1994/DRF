# Generated by Django 4.2.7 on 2023-11-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
