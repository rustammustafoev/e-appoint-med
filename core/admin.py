from django.contrib import admin

from core import models


@admin.register(models.Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Schedule)
class ScheduleModelAdmin(admin.ModelAdmin):
    pass

