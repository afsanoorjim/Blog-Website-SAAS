# Generated by Django 5.1.3 on 2024-11-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="content_image",
            field=models.ImageField(blank=True, null=True, upload_to="blog/media/"),
        ),
    ]
