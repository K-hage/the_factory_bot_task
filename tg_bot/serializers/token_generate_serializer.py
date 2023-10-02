from rest_framework import serializers

from tg_bot.models import TgUser


class TokenGenerateSuccess(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)

    class Meta:
        model = TgUser
        fields = ['token']
