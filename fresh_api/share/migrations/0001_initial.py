# Generated by Django 5.1.3 on 2024-12-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emotions",
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
                ("emotion", models.TextField()),
                ("emotion_color", models.TextField()),
                ("emotion_sticker", models.TextField()),
            ],
        ),
    ]
