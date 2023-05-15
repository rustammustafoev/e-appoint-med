from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication import views


urlpatterns = [
    path('auth/token/', views.CustomTokenObtainPairView.as_view(), name='access-token'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]
