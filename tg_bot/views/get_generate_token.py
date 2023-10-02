from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from tg_bot.models import TgUser
from tg_bot.serializers import TokenGenerateSuccess


class GetGenerateToken(RetrieveAPIView):
    queryset = TgUser.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TokenGenerateSuccess

    def get(self, request, *args, **kwargs):
        tg_user, created = TgUser.objects.get_or_create(
            user=request.user,
        )
        tg_user.set_token()
        tg_user.save(update_fields=['token'])
        return super().get(request, *args, **kwargs)

    def get_object(self):
        return TgUser.objects.filter(user_id=self.request.user.id).first()
