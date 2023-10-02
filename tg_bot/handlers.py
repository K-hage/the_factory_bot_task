from aiogram import types, Router

from aiogram.utils.markdown import text, italic, bold

from tg_bot.utils import binding_token

echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    token = message.text
    chat_id = message.from_user.id
    resp = await binding_token(chat_id, token)
    if resp:
        msg = text(
            italic(resp.get('message')),
            sep='\n')
        await message.answer(msg)
