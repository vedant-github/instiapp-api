# Generated by Django 2.1.5 on 2019-01-31 09:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0002_device_last_refresh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='last_refresh',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=utc)),
        ),
    ]
