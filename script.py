from threading import Thread
from TelegramBotWrapper import TelegramBotWrapper
import generator_wrapper as gw


def run_server():
    # create TelegramBotWrapper instance
    # by default, read parameters in telegram_config.cfg
    tg_server = TelegramBotWrapper(generator_wrapper=gw)
    # by default - read token from extensions/telegram_bot/telegram_token.txt
    tg_server.run_telegram_bot()


def setup():
    Thread(target=run_server).start()
