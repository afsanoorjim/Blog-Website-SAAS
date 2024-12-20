# Generated by Django 5.1.3 on 2024-11-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("author", models.CharField(max_length=4000)),
                ("title", models.CharField(max_length=4000)),
                ("content", models.TextField()),
                ("content_image", models.ImageField(upload_to="")),
                ("publish_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
