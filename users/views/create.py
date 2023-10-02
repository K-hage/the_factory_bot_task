from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
