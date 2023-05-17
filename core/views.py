from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from core import serializers
from core import models
from core import filters
from user.models import Doctor


class AppointmentViewSet(ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)
    filterset_class = filters.AppointmentFilterSet

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.AppointmentSaveSerializer

        return self.serializer_class


class ScheduleViewSet(ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)
    filterset_class = filters.ScheduleFilterSet

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.ScheduleSaveSerializer

        return self.serializer_class


class PrescriptionViewSet(ModelViewSet):
    queryset = models.Prescription.objects.all()
    serializer_class = serializers.PrescriptionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.PrescriptionFilterSet
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.PrescriptionSaveSerializer

        return self.serializer_class


class MedicalRecordViewSet(ModelViewSet):
    queryset = models.MedicalRecord.objects.all()
    serializer_class = serializers.MedicalRecordSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.MedicalRecordSaveSerializer

        return self.serializer_class


class PaymentHistoryViewSet(ModelViewSet):
    queryset = models.PaymentHistory.objects.all()
    serializer_class = serializers.PaymentHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)
    filterset_class = filters.PaymentHistoryFilterSet

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.PaymentHistorySaveSerializer

        return self.serializer_class


class MedicalTestViewSet(ModelViewSet):
    queryset = models.MedicalTest.objects.all()
    serializer_class = serializers.MedicalTestSerializer
    permission_classes = (IsAuthenticated,)


class NotificationViewSet(ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.NotificationSaveSerializer

        return self.serializer_class


class MedicineViewSet(ModelViewSet):
    queryset = models.Medicine.objects.all()
    serializer_class = serializers.MedicineSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return serializers.MedicineSaveSerializer

        return self.serializer_class


class MedicineGroupViewSet(ModelViewSet):
    queryset = models.MedicineGroup.objects.all()
    serializer_class = serializers.MedicineGroupSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)


class HospitalInventoryViewSet(ModelViewSet):
    queryset = models.HospitalInventory.objects.all()
    serializer_class = serializers.HospitalInventorySerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)


class PharmacyViewSet(ModelViewSet):
    queryset = models.Pharmacy.objects.all()
    serializer_class = serializers.PharmacySerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)


class DashboardView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            serializer = serializers.AdminDashboardSerializer(request.data)
        else:
            user = get_object_or_404(Doctor, user=user.id, status=True)
            serializer = serializers.DoctorDashboardSerializer(request.data, context={'doctor': user})

        return Response(serializer.data)
