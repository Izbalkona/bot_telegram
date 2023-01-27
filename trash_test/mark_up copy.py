import random
import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, Filters, MessageHandler, TypeHandler

ask_reply_markuup = ReplyKeyboardMarkup([['Меню']], resize_keyboard = True)



def ask_what_to_do(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Что нужно сделать?',
                             reply_markup=ask_reply_markuup)

def main() -> None:
    updater = Updater("5718308924:AAGXgGQXUh46_z0QNHJzfO6VVQ3YqOHPBKY")


    updater.dispatcher.add_handler(TypeHandler(Update, ask_what_to_do))
    
    updater.start_polling()
    print('Started')
    updater.idle()


if __name__ == "__main__":
    main()