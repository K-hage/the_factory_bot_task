from django.contrib.auth import logout, get_user_model
from rest_framework import (
    permissions,
    status
)
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from users.serializers import LoginSerializer


class LogoutView(DestroyAPIView):
    queryset = get_user_model().objects.all
    serializer_class = LoginSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
