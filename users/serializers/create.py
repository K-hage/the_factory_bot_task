from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers, exceptions


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, validators=[validate_password])
    password_repeat = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'password',
            'password_repeat'
        )

    def create(self, validated_data):
        password = validated_data.get('password')
        password_repeat = validated_data.pop('password_repeat', None)

        if password != password_repeat:
            raise exceptions.ValidationError(
                {'password_repeat': 'Пароли не совпадают'}
            )

        validated_data['password'] = make_password(password)

        user = super().create(validated_data)
        return user
