import datetime
from typing import Tuple

from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.core.exceptions import ValidationError


class ContainerType(models.Model):
    container_type = models.CharField(max_length=200)


    def __str__(self):
        return self.container_type

    class meta:
        verbose_name = 'Booking no.'



class ContainerSpec(models.Model):
    booking_no = models.CharField(max_length=5, blank=False)
    container = models.ForeignKey(ContainerType, on_delete=models.CASCADE, default=0)
    date = models.DateTimeField("pick up date", blank=False, default=datetime.datetime.now())
    booking_date = models.DateTimeField(default=now)
    haulier = models.CharField(max_length=20, blank=False, default=None)
    amount = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(100)])
    container_grade = models.PositiveIntegerField(validators=[
        MaxValueValidator(5)
    ], default=1)
    remarks = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.booking_no


    def get_absolute_url(self):
        return reverse('order:order_detail', kwargs={'get_booking': self.booking_no})



# Create your models here.
