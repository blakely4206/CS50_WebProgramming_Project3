# Generated by Django 3.0.5 on 2020-04-30 03:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20200422_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='pic',
            field=models.ImageField(null=True, upload_to='static/orders/Toppings'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 30, 3, 18, 13, 859312, tzinfo=utc)),
        ),
    ]
