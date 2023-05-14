from django_filters import FilterSet
from django_filters import rest_framework as filters

from core import models


class AppointmentFilterSet(FilterSet):
    ordering = filters.OrderingFilter(fields=[
        'id',
        'status',
    ])
    patient_name = filters.CharFilter(field_name='patient__name', lookup_expr='icontains')

    class Meta:
        model = models.Appointment
        fields = [
            'status',
            'patient_name',
        ]
