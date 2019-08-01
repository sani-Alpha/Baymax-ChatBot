#!/usr/bin/python3
import cgi
import mysql.connector as mariadb
import time
import secrets
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

form1 = cgi.FieldStorage() 
session_id = form1.getvalue('token')

mariadb_connection = mariadb.connect(user='root', password='987', database='db1')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT query  FROM user_data where s_id='"++"'")
data=cursor.fetchall()
passwd=data[0][0]
