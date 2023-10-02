from rest_framework import permissions

from tg_bot.models import TgUser


class IsAuthorized(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return TgUser.objects.filter(user=request.user, chat_id__isnull=False).exists()
