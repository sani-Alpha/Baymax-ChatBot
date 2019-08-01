#!/usr/bin/python3

import cgi 
import mysql.connector as mariadb
form2 = cgi.FieldStorage()

uname = form2.getvalue('number')
password = form2.getvalue('pass')
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

mariadb_connection = mariadb.connect(user='root', password='987', database='db1')
print(1)

cursor = mariadb_connection.cursor()
print(2)

mysqlq='INSERT into users(uname,password) values("'+uname+'","'+password+'")'
print(3)

cursor.execute(mysqlq)
print(4)

mariadb_connection.commit()
print(5)
