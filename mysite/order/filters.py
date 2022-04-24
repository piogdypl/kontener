import django_filters
import django_filters.filters

from .models import ContainerSpec

class OrderFilter(django_filters.FilterSet):
    date = django_filters.filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'placeholder': 'yyyy-mm-dd'}))
    class Meta:
        model = ContainerSpec
        fields = ('booking_no',
                  'container',
                  'date'
                  )