from rest_framework import serializers

from user import models


class HospitalAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.HospitalAdmin
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Nurse
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patient
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'
