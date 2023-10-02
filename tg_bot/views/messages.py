from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from tg_bot.api_sender import send_message_to_telegram_sync
from tg_bot.models import TgUser, Message
from tg_bot.serializers import MessageSerializer, MessagesListSerializer


class SendMessage(CreateAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        tg_user = TgUser.objects.filter(user=request.user).first()
        msg = request.data.get('message')
        send_message_to_telegram_sync(tg_user, msg)
        return super().create(request, *args, **kwargs)


class MessagesListAPI(ListAPIView):
    serializer_class = MessagesListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(
            user=self.request.user
        )
