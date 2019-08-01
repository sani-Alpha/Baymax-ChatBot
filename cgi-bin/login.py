#!/usr/bin/python3
import cgi
import mysql.connector as mariadb
import time
import secrets
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

form1 = cgi.FieldStorage() 
uname = form1.getvalue('username')
fdata = form1.getvalue('password')

mariadb_connection = mariadb.connect(user='root', password='987', database='db1')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT password FROM users where uname='"+uname+"'")
data=cursor.fetchall()
if str(data)=="[]":
	#case when user not found
	print("0")
else:
	passwd=data[0][0]
	if str(passwd)==str(fdata):
        #when login --> True
		s_token=secrets.token_urlsafe(16)
		cursor.execute("SELECT mid FROM session where mid='"+uname+"'")
		data1=cursor.fetchall()
		if str(data1)=="[]":
			mysqlq2="INSERT into session (mid,sid) values('"+uname+"','"+s_token+"')"
			cursor.execute(mysqlq2)
			mariadb_connection.commit()
			print('1,'+s_token)
		else:
			mysqlq2="UPDATE session SET sid='"+s_token+"' WHERE mid='"+uname+"'"
			cursor.execute(mysqlq2)
			mariadb_connection.commit()
			print('1,'+s_token)
