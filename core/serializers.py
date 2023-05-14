from rest_framework import serializers

from core import models
from core import constants


class AppointmentSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Appointment
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()
    patient = serializers.SerializerMethodField()
    scheduled_at = serializers.SerializerMethodField()

    class Meta:
        model = models.Appointment
        fields = '__all__'

    def get_doctor(self, obj: models.Appointment):
        return {
            'id': obj.doctor.id,
            'name': obj.doctor.user.get_full_name()
        }

    def get_patient(self, obj: models.Appointment):
        return {
            'id': obj.patient.id,
            'name': obj.patient.name,
            'email': obj.patient.email,
            'phone_number': obj.patient.phone,
        }

    def get_scheduled_at(self, obj: models.Appointment):
        return {
            'day': obj.scheduled_at.day,
            'from': obj.scheduled_at.from_time,
            'to': obj.scheduled_at.to_time,
        }

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class ScheduleSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Schedule
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = models.Schedule
        fields = '__all__'

    def get_doctor(self, obj: models.Schedule):
        return {
            'id': obj.doctor.id,
            'name': obj.doctor.user.get_full_name()
        }


class MedicineSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Medicine
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    group = serializers.SerializerMethodField()

    class Meta:
        model = models.Medicine
        fields = '__all__'

    def get_group(self, obj: models.Medicine):
        return {
            'id': obj.group.id,
            'title': obj.group.title,
        }


class MedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalTest
        fields = '__all__'


class MedicalRecordSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MedicalRecord
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = models.MedicalRecord
        fields = '__all__'

    def get_patient(self, obj: models.Appointment):
        return {
            'id': obj.patient.id,
            'name': obj.patient.name
        }

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class PrescriptionSaveSerializer(serializers.ModelSerializer):
    medicines = MedicineSaveSerializer(many=True, required=False)
    tests = MedicalTestSerializer(many=True, required=False)

    class Meta:
        model = models.Prescription
        fields = '__all__'

    def update(self, instance, validated_data):
        medicines = validated_data.pop('medicines', [])
        tests = validated_data.pop('tests', [])

        try:
            prescription = super().update(instance, **validated_data)
            self._save_nested(instance, medicines, tests)
        except constants.COMMON_MODEL_EXCEPTIONS as e:
            raise serializers.ValidationError({"error": e})

        return prescription

    def create(self, validated_data):
        medicines = validated_data.pop('medicines', [])
        tests = validated_data.pop('tests', [])

        try:
            prescription = super().create(**validated_data)
            self._save_nested(prescription, medicines, tests)
        except constants.COMMON_MODEL_EXCEPTIONS as e:
            raise serializers.ValidationError({"error": e})

        return prescription

    def _save_nested(self, instance, medicines, tests):
        if medicines:
            self.__save_medicines(instance, medicines)
        if tests:
            self.__save_tests(instance, tests)

    def __save_medicines(self, instance: models.Prescription, data):
        instance.medicines.set([medicine['id'] for medicine in data])

    def __save_tests(self, instance: models.Prescription, data):
        instance.tests.set([test['id'] for test in data])


class PrescriptionSerializer(serializers.ModelSerializer):
    medicines = MedicineSerializer(many=True, read_only=True)
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()
    tests = MedicalTestSerializer(many=True, read_only=True)
    medical_record = MedicalRecordSerializer(read_only=True)

    class Meta:
        model = models.Prescription
        fields = '__all__'

    def get_doctor(self, obj: models.Prescription):
        return {
            'id': obj.doctor.id,
            'name': obj.doctor.user.get_full_name()
        }

    def get_patient(self, obj: models.Prescription):
        return {
            'id': obj.patient.id,
            'name': obj.patient.name
        }

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class PaymentHistorySaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PaymentHistory
        fields = '__all__'


class PaymentHistorySerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = models.PaymentHistory
        fields = '__all__'

    def get_patient(self, obj: models.Prescription):
        return {
            'id': obj.patient.id,
            'name': obj.patient.name,
            'email': obj.patient.email,
        }


class NotificationSaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Notification
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()
    patient = serializers.SerializerMethodField()

    class Meta:
        model = models.Notification
        fields = '__all__'

    def get_doctor(self, obj: models.Prescription):
        return {
            'id': obj.doctor.id,
            'name': obj.doctor.user.get_full_name()
        }

    def get_patient(self, obj: models.Prescription):
        return {
            'id': obj.patient.id,
            'name': obj.patient.name
        }


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
