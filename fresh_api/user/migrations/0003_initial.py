# Generated by Django 5.1.3 on 2024-12-02 07:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0002_delete_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=50, unique=True)),
                ("nickname", models.CharField(max_length=25)),
                ("uuid", models.UUIDField(default=uuid.uuid4)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "user_role",
                    models.IntegerField(
                        choices=[(0, "일반 유저"), (1, "멘토"), (2, "어드민")], default=0
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
