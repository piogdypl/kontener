from django import forms
from .models import ContainerSpec

class CreateOrder(forms.ModelForm):

    class Meta:
        model = ContainerSpec
        fields = '__all__'
        exclude = ('booking_date',)

