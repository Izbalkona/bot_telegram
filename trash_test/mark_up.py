import random
import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler, Filters, MessageHandler, TypeHandler

ask_reply_markuup = ReplyKeyboardMarkup([['Случайное число']], resize_keyboard = True)


number_inline_keyboard_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("ген новое", callback_data='new_random_number')]
    ])


def get_random_number():
    return random.randint(0, 10)

def random_number(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(get_random_number(), reply_markup=number_inline_keyboard_markup)

def ask_what_to_do(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Что нужно сделать?',
                             reply_markup=ask_reply_markuup)


def new_random_number(update: Update, context: CallbackContext) -> None:
    text = f'{get_random_number()}\nОтредактировано: {datetime.datetime.now().isoformat()}'
    update.callback_query.edit_message_text(text=text, reply_markup=number_inline_keyboard_markup)


def main() -> None:
    updater = Updater("5718308924:AAFDDxwBvSoOXZJHOZICW75RZPLD2pSO668")
 
    updater.dispatcher.add_handler(CallbackQueryHandler(new_random_number, pattern='^new_random_number'))
    
    updater.dispatcher.add_handler(
        MessageHandler(Filters.update.message & Filters.text('Случайное число'), random_number))
    
    updater.dispatcher.add_handler(TypeHandler(Update, ask_what_to_do))
    
    updater.start_polling()
    print('Started')
    updater.idle()


if __name__ == "__main__":
    main()