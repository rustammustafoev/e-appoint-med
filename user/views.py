from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from user import serializers
from user import models
from user import filters


class HospitalAdminViewSet(ModelViewSet):
    queryset = models.HospitalAdmin.objects.all()
    serializer_class = serializers.HospitalAdminSerializer
    filter_backends = (DjangoFilterBackend,)
    # permission_classes = (IsAuthenticated,)


class DoctorViewSet(ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return serializers.DoctorSaveSerializer

        return self.serializer_class


class NurseViewSet(ModelViewSet):
    queryset = models.Nurse.objects.all()
    serializer_class = serializers.NurseSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)


class PatientViewSet(ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.PatientFilterSet
    permission_classes = (IsAuthenticated,)


class DepartmentViewSet(ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsAuthenticated,)
