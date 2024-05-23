# Generated by Django 5.0 on 2024-05-22 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0005_rename_active_driver_available_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EWallet",
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
                ("amount", models.FloatField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ewallet",
                        to="user.myuser",
                    ),
                ),
            ],
        ),
    ]
