# Generated by Django 3.0.5 on 2020-04-09 06:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20200409_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 9, 6, 44, 58, 69269, tzinfo=utc)),
        ),
    ]
