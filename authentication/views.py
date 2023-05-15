from rest_framework_simplejwt.views import TokenObtainPairView

from authentication import serializers


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer
