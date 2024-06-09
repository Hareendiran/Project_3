# Generated by Django 5.0.2 on 2024-03-24 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("physics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhysicsContent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="physics/content-images/")),
                ("content", models.TextField()),
            ],
        ),
    ]
