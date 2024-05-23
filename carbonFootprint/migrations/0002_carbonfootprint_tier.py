# Generated by Django 5.0 on 2024-05-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carbonFootprint", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carbonfootprint",
            name="tier",
            field=models.CharField(
                choices=[
                    ("No Tier", "No Tier"),
                    ("Bronze", "Bronze"),
                    ("Silver", "Silver"),
                    ("Gold", "Gold"),
                ],
                default="No Tier",
                max_length=255,
            ),
        ),
    ]