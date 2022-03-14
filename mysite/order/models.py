import datetime
from django.db import models
from django.utils import timezone

class ContainerType(models.Model):
    container_type = models.CharField(max_length=200)
    container_grade = models.IntegerField(default=0)
    def __str__(self):
        return self.container_type

class PickUpDate(models.Model):
   # container = models.ForeignKey(ContainerType, on_delete=models.CASCADE)
    date = models.DateTimeField("Data podjęcia kontenera")
    pickup_time = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_txt
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)






# Create your models here.
