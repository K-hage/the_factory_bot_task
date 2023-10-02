import asyncio

from aiogram.utils.markdown import text, italic, bold

from tg_bot.management.commands.runbot import Command


async def send_message_to_telegram(chat_id, msg):
    bot = Command().get_bot()
    await bot.send_message(chat_id=chat_id, text=msg)
    await bot.session.close()


def send_message_to_telegram_sync(tg_user, message_text):
    msg = text(
        italic(f'{tg_user.user.username}, я получил от тебя сообщение:'),
        bold(message_text),
        sep='\n')
    asyncio.run(send_message_to_telegram(tg_user.chat_id, msg))
