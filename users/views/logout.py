from django.contrib.auth import logout
from rest_framework import (
    permissions,
    status
)
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response


class LogoutView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
