#!/usr/bin/python3
import cgi
import mysql.connector as mariadb
import time
import secrets
print('Set-Cookie: sid='+str(time.time()))
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

form1 = cgi.FieldStorage() 
token = form1.getvalue('token')

mariadb_connection = mariadb.connect(user='root', password='987', database='db1')
cursor = mariadb_connection.cursor()
cursor.execute("SELECT * FROM session where sid='"+token+"'")
data=cursor.fetchall()
passwd=data[0][1]
if str(passwd)==str(token):
	#when login --> True
	print('1')
else:
	#when login is Wrong	
	print('0')
