from django.contrib import admin

from core import models


@admin.register(models.Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Schedule)
class ScheduleModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Prescription)
class PrescriptionModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicalRecord)
class MedicalRecordModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PaymentHistory)
class PaymentHistoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicalTest)
class MedicalTestModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Notification)
class NotificationModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Medicine)
class MedicineModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HospitalInventory)
class HospitalInventoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Pharmacy)
class PharmacyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicineInStock)
class MedicineInStockModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MedicineGroup)
class MedicineGroupModelAdmin(admin.ModelAdmin):
    pass
