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


class ScheduleFilterSet(FilterSet):
    ordering = filters.OrderingFilter(fields=[
        'id', 'from_time', 'to_time'
    ])
    doctor_name = filters.CharFilter(method='filter_by_doctor_full_name', lookup_expr='icontains')

    class Meta:
        model = models.Schedule
        fields = [
            'doctor_name',
            'day',
        ]

    def filter_by_doctor_full_name(self, queryset, name, value):
        return queryset.filter(user__full_name__icontains=value)


class PrescriptionFilterSet(FilterSet):
    ordering = filters.OrderingFilter(fields=[
        'id',
        'created_at',
        'updated_at',
    ])
    patient_name = filters.CharFilter(field_name='patient__name', lookup_expr='icontains')
    medicines = filters.CharFilter(method='filter_by_medicine_names')
    tests = filters.CharFilter(method='filter_by_test_names')
    comments = filters.CharFilter(field_name='comments', lookup_expr='icontains')
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = models.Prescription
        fields = [
            'patient_name',
            'medicines',
            'tests',
            'comments',
            'created_at',
            'updated_at',
        ]

    def filter_by_medicine_names(self, queryset, name, value):
        medicine_names = value.split(',')

        return queryset.objects.filter(medicines__name__in=medicine_names)

    def filter_by_test_names(self, queryset, name, value):
        test_names = value.split(',')

        return queryset.objects.filter(tests__title__in=test_names)
