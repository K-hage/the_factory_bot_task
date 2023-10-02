from django.contrib.auth import authenticate, get_user_model
from rest_framework import (
    exceptions,
    serializers
)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password'
        )

    def create(self, validated_data):
        user = authenticate(
            username=validated_data['username'],
            password=validated_data['password']
        )
        if not user:
            raise exceptions.AuthenticationFailed('Имя пользователя или пароль некорректны')

        return user
