# Generated by Django 3.0.4 on 2020-04-07 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza_Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza_Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza_Topping_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_type', models.CharField(max_length=20)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza_Size')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza_Style')),
                ('topping_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza_Topping_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('pizza_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza_Type')),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('contents', models.ManyToManyField(blank=True, to='orders.Pizza')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
