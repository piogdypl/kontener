# Generated by Django 4.0.3 on 2022-03-27 17:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_type', models.CharField(max_length=200)),
                ('container_grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ContainerSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_no', models.CharField(blank=True, max_length=15)),
                ('date', models.DateTimeField(verbose_name='Data podjęcia kontenera')),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pickup_time', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('container', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.containertype')),
            ],
        ),
    ]
