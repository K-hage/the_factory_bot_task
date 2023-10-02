import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from django.conf import settings
from django.core.management import BaseCommand

from tg_bot.main import main


class Command(BaseCommand):
    help = 'run bot'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._token = settings.TELEGRAM_BOT_TOKEN
        self._storage = MemoryStorage()
        self._bot = Bot(self._token, parse_mode=ParseMode.MARKDOWN)
        self._dp = Dispatcher(storage=self._storage)

    def get_bot(self):
        return self._bot

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO)

        try:
            asyncio.run(main(self._bot, self._dp))
        except KeyboardInterrupt:
            self.stdout.write('Bot was stopped!')
