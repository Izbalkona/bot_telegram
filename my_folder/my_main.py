#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging 

import pymysql
import pymysql.cursors

from my_sql import *# важен порядок вызова библиотек
from my_main_bible import *
from my_settings import *




from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter, TypeHandler
 




def main() -> None:
    check_sqlbase()
    
    #send_photo(bot, chat_id)#отправляет фото
    
    tprint(time_now())#отправляет сообщение
    
    updater = Updater("5718308924:AAFDDxwBvSoOXZJHOZICW75RZPLD2pSO668") #connect Telegam
    logging.info('start_bot'+'-'*20)

    
    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(CommandHandler("registration", registration_command))
    

    
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('запросить данные'), rem_pas))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('привет'), ru))


    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('привет'), ru))
    updater.dispatcher.add_handler(TypeHandler(Update, echo))# должно быть последним

    updater.start_polling() # цикл
    print('Started')
    updater.idle()
       
if __name__ == "__main__":
    main()