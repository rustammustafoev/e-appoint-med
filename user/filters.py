from django_filters import FilterSet
from django_filters import rest_framework as filters

from user import models


class PatientFilterSet(FilterSet):
    ordering = filters.OrderingFilter(field_name=[
        'name', 'age', 'gender', 'id',
    ])
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    email = filters.CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = models.Patient
        fields = [
            'name',
            'age',
            'gender',
            'email',
        ]
