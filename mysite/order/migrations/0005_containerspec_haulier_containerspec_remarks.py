# Generated by Django 4.0.3 on 2022-04-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_containerspec_container_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerspec',
            name='haulier',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='containerspec',
            name='remarks',
            field=models.TextField(default=None),
        ),
    ]