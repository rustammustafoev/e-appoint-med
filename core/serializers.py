from rest_framework import serializers

from core import models


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Appointment
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prescription
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalRecord
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'


class MedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalTest
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicine
        fields = '__all__'


class MedicineGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicineGroup
        fields = '__all__'


class HospitalInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HospitalInventory
        fields = '__all__'


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pharmacy
        fields = '__all__'
