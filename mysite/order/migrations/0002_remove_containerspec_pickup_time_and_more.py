# Generated by Django 4.0.3 on 2022-03-27 18:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='containerspec',
            name='pickup_time',
        ),
        migrations.AlterField(
            model_name='containerspec',
            name='amount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='containerspec',
            name='booking_no',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='containertype',
            name='container_grade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
