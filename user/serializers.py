from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction

from user import models
from user import services
from core import constants


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class HospitalAdminSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.HospitalAdmin
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        user = validated_data.get('user')

        try:
            user = services.create_user(user)
            validated_data['user'] = user.id
            hospital_admin = super().create(**validated_data)
        except constants.COMMON_MODEL_EXCEPTIONS as e:
            raise serializers.ValidationError({"error": e})

        return hospital_admin

    @transaction.atomic
    def update(self, instance, validated_data):
        user = validated_data.get('user')
        if user:
            user = validated_data.pop('user')

        try:
            hospital_admin = services.update_user(instance, user)
        except constants.COMMON_MODEL_EXCEPTIONS as e:
            raise serializers.ValidationError({"error": e})

        return hospital_admin


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department = serializers.SerializerMethodField()

    class Meta:
        model = models.Doctor
        fields = '__all__'

    def get_department(self, obj: models.Doctor):
        return {
            'id': obj.department.id,
            'title': obj.department.title,
        }


class DoctorSaveSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Doctor
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        user = validated_data.get('user')

        try:
            user = services.create_user(user)
            validated_data['user'] = user.id
            doctor = super().create(**validated_data)
        except constants.COMMON_MODEL_EXCEPTIONS as e:
            raise serializers.ValidationError({"error": e})

        return doctor

    @transaction.atomic
    def update(self, instance, validated_data):
        user = validated_data.get('user')
        if user:
            user = validated_data.pop('user')

        try:
            doctor = services.update_user(instance, user)
        except constants.COMMON_MODEL_EXCEPTIONS as e:
            raise serializers.ValidationError({"error": e})

        return doctor


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
