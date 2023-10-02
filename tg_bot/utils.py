from asgiref.sync import sync_to_async

from tg_bot.models import TgUser


@sync_to_async
def binding_token(chat_id, token):
    tg_user: TgUser = TgUser.objects.filter(token=token).first()
    if tg_user:
        tg_user.chat_id = chat_id
        tg_user.save(update_fields=['chat_id'])
        return {'message': 'Токен подтвержден'}
