# Generated by Django 4.0.3 on 2022-04-24 09:47

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_containerspec_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containerspec',
            name='date',
            field=models.DateTimeField(default=datetime.date(2000, 1, 1), validators=[django.core.validators.MinValueValidator(1650793585)], verbose_name='pick up date'),
        ),
    ]
