#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import logging

from my_main_bible import tprint

import pymysql
import pymysql.cursors


user_table = 'exam_users'

def user_request_cell(cursor, user_name, user_password, user_var): #выводит любую информаци о пользователе по ключу user_name 
    try:
        select_all_rows = f"SELECT {user_var}, password FROM {user_table} where name = '{user_name}'"
        per = cursor.execute(select_all_rows)
        results = cursor.fetchall()
        if results == ():
            message = 'Такого пользователя нет'
        elif str(results[0]["password"]) != user_password:
            message = f"неверный пароль"
        elif results != ():
            message =f"ваш запрос: {results[0][user_var]}"
        else:
            message = 'нет такого'
            tprint('нет такого')
        tprint(message)
        logging.info(f"203: пользователь ({user_name}) запрашивал данные ({user_var}) : результат ({message})")
    except Exception as req_err:
        print("Connection refused...")
        print(str(req_err))
        tprint("Connection refused...")
        tprint(str(req_err))



def my_sql_insert(cursor, user_mail): #добавляет нового пользователя
    try:
        cursor.execute("INSERT INTO exam_users (name, password,mail,date) VALUES ('dima','pkol111', %s ,'23111') ;", user_mail)
    except Exception as req_err:
        print("Connection refused...")
        print(str(req_err))
        tprint(str(req_err))
        logging.info(f'ошибка = {req_err}')



def check_sqlbase(user_name, user_password, user_var): #связь my_main с sql
    try:
        connection = pymysql.connect(host='localhost',
            user='root',
            password='root',
            db='test_bd',
            port=8889,
            cursorclass=pymysql.cursors.DictCursor)
        print('succ')
        try:
            with connection.cursor() as cursor:
                user_request_cell(cursor, user_name, user_password, user_var) #выводит любую информаци о пользователе по ключу user_name и соотвествию user_password
                #my_sql_insert(cursor, user_mail) #добавляет нового пользователя
        finally:
            connection.close()


    except Exception as ex:
        print("Connection refused...")
        print(ex)
