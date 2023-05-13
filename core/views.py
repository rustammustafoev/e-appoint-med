from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from core import serializers
from core import models
from core import filters


class AppointmentViewSet(ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class ScheduleViewSet(ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class PrescriptionViewSet(ModelViewSet):
    queryset = models.Prescription.objects.all()
    serializer_class = serializers.PrescriptionSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class MedicalRecordViewSet(ModelViewSet):
    queryset = models.MedicalRecord.objects.all()
    serializer_class = serializers.MedicalRecordSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class PaymentViewSet(ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class MedicalTestViewSet(ModelViewSet):
    queryset = models.MedicalTest.objects.all()
    serializer_class = serializers.MedicalTestSerializer
    # permission_classes = (IsAuthenticated,)


class NotificationViewSet(ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class MedicineViewSet(ModelViewSet):
    queryset = models.Medicine.objects.all()
    serializer_class = serializers.MedicineSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class MedicineGroupViewSet(ModelViewSet):
    queryset = models.MedicineGroup.objects.all()
    serializer_class = serializers.MedicineGroupSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class HospitalInventoryViewSet(ModelViewSet):
    queryset = models.HospitalInventory.objects.all()
    serializer_class = serializers.HospitalInventorySerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class PharmacyViewSet(ModelViewSet):
    queryset = models.Pharmacy.objects.all()
    serializer_class = serializers.PharmacySerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)
