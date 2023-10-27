# Generated by Django 3.2.10 on 2023-01-11 12:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("locations", "0014_location_str_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="LocationLocationDistance",
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
                ("distance", models.FloatField(default=100000000)),
                (
                    "location1",
                    models.ForeignKey(
                        default=uuid.uuid4,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lld1",
                        to="locations.location",
                    ),
                ),
                (
                    "location2",
                    models.ForeignKey(
                        default=uuid.uuid4,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lld2",
                        to="locations.location",
                    ),
                ),
            ],
            options={
                "verbose_name": "Location-Location Distance",
                "verbose_name_plural": "Location-Location Distances",
            },
        ),
        migrations.AddField(
            model_name="location",
            name="adjacent_locs",
            field=models.ManyToManyField(
                blank=True,
                related_name="adjacent_loc",
                through="locations.LocationLocationDistance",
                to="locations.Location",
            ),
        ),
    ]
