import re
import time
from telegram import Bot, Update
import my_main_bible
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter



def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
    Бот может здороваться на разных языках.
    Список поддерживаемых приветствий:
    - привет - русский
    - hello - английский
    - hola - испанский
    """)

chat_id = 642411623 #замените на свое значение, подробнее ниже
bot = Bot("5718308924:AAFDDxwBvSoOXZJHOZICW75RZPLD2pSO668")

def ru(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('привет')


def get_greeting_filter(greeting: str) -> BaseFilter:
    return Filters.regex(re.compile(f'^{greeting}$', re.IGNORECASE)) & Filters.update.message


def main() -> None:
    my_main_bible.send_photo(bot, chat_id)#отправляет фото
    my_main_bible.tprint('der')#отправляет сообщение

    updater = Updater("5718308924:AAFDDxwBvSoOXZJHOZICW75RZPLD2pSO668")
    
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('привет'), ru))


    updater.start_polling()
    print('Started')
    updater.idle()
    

    print('Cat has been sent')
    
if __name__ == "__main__":
    main()