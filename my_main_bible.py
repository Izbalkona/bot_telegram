import time
from telegram import Bot, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter

chat_id = 642411623 #замените на свое значение, подробнее ниже
bot = Bot("5718308924:AAFDDxwBvSoOXZJHOZICW75RZPLD2pSO668")


def send_photo(bot, chat_id): #отправляет фотку кота
    url = f'https://yandex.ru/images/search?from=tabbar&text=skyrim{time.time()}'
    bot.send_photo(chat_id, url)


def tprint(saw):
    bot.send_message(chat_id, saw)