import logging 

import pymysql
import pymysql.cursors

from my_main_bible import *
from my_sql import *

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter




logging.basicConfig(level=logging.INFO, filename="py_log.log",
                    format="%(asctime)s %(levelname)s %(message)s")# настройка логов

