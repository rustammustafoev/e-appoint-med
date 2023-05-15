from django.contrib import admin

from user import models


@admin.register(models.HospitalAdmin)
class HospitalModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Patient)
class PatientModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Department)
class DepartmentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Nurse)
class NurseModelAdmin(admin.ModelAdmin):
    pass
