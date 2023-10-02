from django.urls import path

from users.views import UserCreateAPIView, LoginView, LogoutView

urlpatterns = [
    path('create_user/', UserCreateAPIView.as_view(), name='create_user'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
