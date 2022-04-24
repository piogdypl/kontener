# Generated by Django 4.0.3 on 2022-04-23 17:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_containerspec_pickup_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='containertype',
            name='container_grade',
        ),
        migrations.AddField(
            model_name='containerspec',
            name='container_grade',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
