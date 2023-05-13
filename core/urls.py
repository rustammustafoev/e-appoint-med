from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views


router = DefaultRouter()
router.register('appointment', views.AppointmentViewSet)
router.register('schedule', views.ScheduleViewSet)
router.register('prescription', views.PrescriptionViewSet)
router.register('medical/record', views.MedicalRecordViewSet)
router.register('payment', views.PaymentViewSet)
router.register('medical/test', views.MedicalTestViewSet)
router.register('notification', views.NotificationViewSet)
router.register('medicine', views.MedicineViewSet)
router.register('medicine/group', views.MedicineGroupViewSet)
router.register('hospital/inventory', views.HospitalInventoryViewSet)
router.register('pharmacy', views.PharmacyViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
