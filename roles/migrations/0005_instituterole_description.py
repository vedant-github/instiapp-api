# Generated by Django 2.0.2 on 2018-03-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roles", "0004_auto_20180324_1206"),
    ]

    operations = [
        migrations.AddField(
            model_name="instituterole",
            name="description",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
