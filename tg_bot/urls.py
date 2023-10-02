from django.urls import path

from tg_bot import views

urlpatterns = [
    path('tg_token/', views.GetGenerateToken.as_view()),
    path('send_message/', views.SendMessage.as_view()),
    path('list_messages/', views.MessagesListAPI.as_view()),
]
