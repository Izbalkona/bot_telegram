#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import pymysql
import pymysql.cursors

try:
    con = pymysql.connect(host='localhost',
        user='root',
        password='root',
        db='test_bd',
        port=8889,
        cursorclass=pymysql.cursors.DictCursor)
    print('succ')
except Exception as ex:
    print("Connection refused...")
    print(ex)
