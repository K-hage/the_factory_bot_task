from aiogram import Bot, Dispatcher

from tg_bot.handlers import echo_router


async def main(bot: Bot, dp: Dispatcher) -> None:
    dp.include_router(echo_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
