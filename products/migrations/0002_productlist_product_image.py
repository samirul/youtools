# Generated by Django 5.1.1 on 2025-01-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productlist",
            name="product_image",
            field=models.ImageField(default="", upload_to="media/products/images/"),
            preserve_default=False,
        ),
    ]
