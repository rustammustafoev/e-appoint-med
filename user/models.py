from django.db import models
from django.contrib.auth.models import User


class Gender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    OTHER = 'O', 'Other'


class HospitalAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year_of_experience = models.PositiveIntegerField()
    phone = models.CharField(max_length=50)
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=1, choices=Gender.choices)

    class Meta:
        db_table = 'doctor'
        managed = False

    def __str__(self):
        return self.user.get_full_name()


class Nurse(models.Model):
    name = models.CharField(max_length=100)
    year_of_experience = models.PositiveIntegerField()
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'nurse'
        managed = False

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    email = models.CharField(max_length=100)
    passport_id = models.CharField(max_length=7, help_text='Passport ID is consist of 7 characters')
    address = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=20, help_text='DD-MM-YYYY')

    class Meta:
        db_table = 'patient'
        managed = False

    def __str__(self):
        return self.name


class Department(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'hospital_department'
        managed = False

    @property
    def total_employee_amount(self):
        pass

    def __str__(self):
        return self.title
