#!/usr/bin/python3
# -*- coding: utf-8 -*-

user_mail = 'sder'
 
import pymysql
import pymysql.cursors
def my_sql_insert(user_mail):

    cursor.execute("INSERT INTO exam_users (name, password,mail,date) VALUES ('dima','pkol111', %s ,'23111') ;", user_mail)

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
            #cursor.execute("CREATE TABLE po (id int AUTO_INCREMENT, name varchar(32), PRIMARY KEY (id));")
            #cursor.execute("INSERT INTO exam_users (name, password,mail,date) VALUES ('dima','pkol111','qwwer','23111');")

            my_sql_insert(user_mail)
            print("suc")
    finally:
        connection.close()


except Exception as ex:
    print("Connection refused...")
    print(f"ex={ex}")