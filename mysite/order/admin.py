from django.contrib import admin
from .models import ContainerType, ContainerSpec
from django import forms

# admin.site.register(ContainerType)
@admin.register(ContainerType)
class Cont(admin.ModelAdmin):
    search_fields = [
        'booking_no',
    ]

@admin.register(ContainerSpec)
class Order(admin.ModelAdmin):
    list_display = (
        'booking_no',
        'container',
        'date',
        'booking_date',
        'amount',
    )
    list_filter = (
        'booking_no',
        'container',
        'date',
        'booking_date',
        'amount',
    )
    search_fields = [
        'booking_no',
    ]
    # prepopulated_fields = {'booking_no':('container',)}
# Register your models here.


