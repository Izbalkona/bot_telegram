#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import pymysql
import pymysql.cursors

from my_main_bible import *

user_name='dima'
user_var='mail'
user_mail='adeeer'


def user_request_cell(cursor, name, user_var):
    select_all_rows = "SELECT * FROM exam_users"
    cursor.execute(select_all_rows)
    user_date=cursor.fetchall()
    try:
        for id_user in user_date:
            for i,r in id_user.items():
                if r == user_name:
                    tprint(f'{id_user[user_var]}')
        print('+'*20)
    except Exception as req_err:
        print("Connection refused...")
        print(str(req_err))
        tprint("Connection refused...")
        tprint(str(req_err))
    finally:
            tprint(f"Ваш запрос {name}: {user_var}")



def my_sql_insert(cursor, user_mail): #позволяет создать нового пользователя
    try:
        cursor.execute("INSERT INTO exam_users (name, password,mail,date) VALUES ('dima','pkol111', %s ,'23111') ;", user_mail)
    except Exception as req_err:
        print("Connection refused...")
        print(str(req_err))
        tprint("Connection refused...")
        tprint(str(req_err))



def check_sqlbase(): #связь my_main с sql
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
                user_request_cell(cursor, user_name, user_var) #выводит любую информаци о пользователе по ключу user_name
                my_sql_insert(cursor, user_mail) #добавляет нового пользователя
        finally:
            connection.close()


    except Exception as ex:
        print("Connection refused...")
        print(ex)
