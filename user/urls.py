from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views


router = DefaultRouter()
router.register('admin', views.HospitalAdminViewSet)
router.register('doctor', views.DoctorViewSet)
router.register('nurse', views.NurseViewSet)
router.register('patient', views.PatientViewSet)
router.register('department', views.DepartmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]