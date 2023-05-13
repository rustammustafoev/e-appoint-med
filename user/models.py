from django.db import models
from django.contrib.auth.models import User


class HospitalAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_experience = models.PositiveIntegerField()
    phone = models.CharField(max_length=50)
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'doctor'


class Nurse(models.Model):
    name = models.CharField(max_length=100)
    year_of_experience = models.PositiveIntegerField()
    phone = models.CharField(max_length=50)

    class Meta:
        db_table = 'nurse'


class Patient(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'patient'


class Department(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'hospital_department'

    @property
    def total_employees_amount(self):
        pass
