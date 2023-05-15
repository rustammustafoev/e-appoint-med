from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_admin'] = user.is_superuser
        token['username'] = user.username

        return token
