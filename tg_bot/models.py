from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.db import models


class TgUser(models.Model):
    chat_id = models.PositiveBigIntegerField(
        verbose_name='id пользователя',
        blank=True,
        null=True
    )
    token = models.CharField(
        max_length=255,
        verbose_name='токен пользователя',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.user)

    def set_token(self):
        self.token = default_token_generator.make_token(self.user)


class Message(models.Model):
    message = models.CharField(
        max_length=255,
        verbose_name='Сообщение'
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Отправитель'
    )
    data_joined = models.DateField(
        auto_now_add=True,
        verbose_name='Дата отправки'
    )

    def __str__(self):
        return self.message[:10]
