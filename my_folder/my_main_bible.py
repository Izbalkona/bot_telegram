import re
import time
import datetime

from my_settings import *

from telegram import Bot, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter, TypeHandler

chat_id = 642411623 
bot = Bot("5718308924:AAFDDxwBvSoOXZJHOZICW75RZPLD2pSO668")
passw = '321'
image='cup'

def time_now():
    time = datetime.datetime.today().strftime("%Y-%m-%d  %H:%M:%S")
    return str(time)

def send_photo(bot, chat_id): #отправляет фотку 
    url = f'https://yandex.ru/images/search?from=tabbar&text={image}{time.time()}'
    bot.send_photo(chat_id, url)


def tprint(saw): #send message
    bot.send_message(chat_id, saw,  parse_mode='html' )


def get_greeting_filter(greeting: str) -> BaseFilter:
    return Filters.regex(re.compile(f'^{greeting}$', re.IGNORECASE)) & Filters.update.message


def ru(update: Update, context: CallbackContext) -> None: #callBack
    update.message.reply_text('привет')


def rem_pas(update: Update, context: CallbackContext) -> None: #callBack
    
    update.message.reply_text('твой пароль: '+ passw)
    tprint(time_now())
    
def help_command(update: Update, context: CallbackContext) -> None: #описание функций
    update.message.reply_text("""
    /registration - регистрация нового пльзователя
    Бот может здороваться на разных языках.
    Список поддерживаемых приветствий:
    - привет - русский
    - hello - английский
    - hola - испанский
    """)

def registration_command(update: Update, context: CallbackContext) -> None: #описание функций
    update.message.reply_text(""" Введите ваш логин:
    """)

def echo(update: Update, context: CallbackContext) -> None: #регистрация любого сообщения
    tprint(f'Ваш запрос - <b>({update.message.text})</b> - не понятен для меня')
    logging.info(f'нераспознанный текст {update.message.text}')