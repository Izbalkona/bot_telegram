#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import pymysql
import pymysql.cursors

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
            cursor.execute("SHOW DATABASES;")
            print(cursor.fetchall())
            select_all_rows = "SELECT * FROM exam_users"
            cursor.execute(select_all_rows)
            rows=cursor.fetchall()
            for row in rows:
                print(row)
            print('+'*20)
    finally:
        connection.close()


except Exception as ex:
    print("Connection refused...")
    print(ex)

#https://www.youtube.com/watch?v=LS42t1VMwuM&ab_channel=PythonToday