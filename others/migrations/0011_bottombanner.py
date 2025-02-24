# Generated by Django 5.1.1 on 2025-02-23 13:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("others", "0010_alter_aboutus_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BottomBanner",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("banner_image", models.ImageField(upload_to="media/homepage")),
                ("banner_text", models.TextField(max_length=500)),
            ],
            options={
                "verbose_name_plural": "Bottom banner",
            },
        ),
    ]
