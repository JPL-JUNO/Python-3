# Generated by Django 5.1.1 on 2024-09-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0004_category_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(),
        ),
    ]