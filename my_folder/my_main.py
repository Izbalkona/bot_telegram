#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re

import pymysql
import pymysql.cursors

from my_sql import * # важен порядок вызова библиотек
from my_main_bible import *
from my_settings import *




from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter, TypeHandler, ConversationHandler

def start(update, context):
    # Сразу задаём первый вопрос, а ответ уже смотрим в первом обработчике
    update.message.reply_text("""
    Бот может выдать данные пользователя:
    Список поддерживаемых команд:
    -------------------------------
    1 - мой mail
    2 - количество слов на аккаунте
    -------------------------------
    В запросе указать номер команды
    """)
    # Число-ключ в словаре states ConversationHandler
    # Оно указывает, что дальше на сообщения от этого пользователя должен отвечать обработчик states[1]
    # До этого момента обработчиков текстовых сообщений
    # для этого пользователя не было,
    # поэтому текстовые сообщения игнорировались    
    return 1

def first_response(update, context: CallbackContext):
    # Ответ вопрос, заданный в /start
    answer = update.message.text
    if answer.lower() == '1' or answer.lower() == '2':
        # Задаём новый вопрос, а ответ обрабатываем в обработчике 2
        update.message.reply_text('Тогда напиши, свой пароль:')
        global user_var
        if answer.lower() == '1':
            user_var = 'mail'
        elif answer.lower() == '2':
            user_var = 'words'
        return 2
    else:
        update.message.reply_text('Ну, как хочешь...')
        return ConversationHandler.END


def second_response(update, context: CallbackContext):
    # Ответ на второй вопрос
    user_name = update.message.chat.id
    user_password = update.message.text
    check_sqlbase(user_name, user_password, user_var)
    # Константа, означающая конец диалога
    # Все обработчики из states и fallbacks становятся неактивными
    return ConversationHandler.END 
    

def stop(update, context):
    update.message.reply_text("Жаль. А было бы интересно пообщаться. Хорошего дня!")
    return ConversationHandler.END

conv_handler = ConversationHandler(
    # Точка входа в диалог.
    # В данном случае — команда /start. Она задаёт первый вопрос.
    entry_points=[CommandHandler('start', start)],
    
    # Словарь состояний внутри диалога. 
    # Наш вариант с двумя обработчиками,
    # фильтрующими текстовые сообщения.
    states={
    # Функция читает ответ на первый вопрос и задаёт второй.
    1: [MessageHandler(Filters.text, first_response)],
    # Функция читает ответ на второй вопрос и завершает диалог.
    2: [MessageHandler(Filters.text, second_response)]
    },

# Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)



def main() -> None:
    
    send_photo(bot, chat_id)#отправляет фото
    
    tprint(time_now())#отправляет сообщение
    
    updater = Updater("5718308924:AAGXgGQXUh46_z0QNHJzfO6VVQ3YqOHPBKY") #connect Telegam
    #logging.info('start_bot'+'-'*20)

    updis = updater.dispatcher
    
    
    updis.add_handler(MessageHandler(get_greeting_filter('привет'), ru))
    
    updis.add_handler(conv_handler)

    updis.add_handler(CommandHandler('start', start))
    updis.add_handler(CommandHandler('stop', stop))
    updis.add_handler(CommandHandler("help", help_command))
    updis.add_handler(CommandHandler("registration", registration_command))
    
    
    updater.dispatcher.add_handler(TypeHandler(Update, echo))# должно быть последним


    updater.start_polling()
    print('Started')
    updater.idle()


if __name__ == "__main__":
    main()