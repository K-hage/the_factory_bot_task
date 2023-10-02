from rest_framework import serializers

from tg_bot.models import Message


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    message = serializers.CharField(
        max_length=255,
        required=True
    )

    class Meta:
        model = Message
        fields = [
            'message',
            'user'
        ]


class MessagesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'message',
            'data_joined'
        ]
