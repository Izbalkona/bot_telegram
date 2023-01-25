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
        with connection.cursor as cursor:
            create_table_query = "CREATE TABLE 'users'(id int AUTO_INCREMENT, name varachar(32), password varcar(32), email varchar(32), PRIMARY KEY(id));"
                                
            cursor.execute(create_table_query)
            print('table succ!!')

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)

#https://www.youtube.com/watch?v=LS42t1VMwuM&ab_channel=PythonToday