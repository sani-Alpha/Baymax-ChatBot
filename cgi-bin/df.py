#!/usr/bin/python3
import cgi
import mysql.connector as mariadb
import time
import requests
import json
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

form1 = cgi.FieldStorage()
q = form1.getvalue('q')
s_id=form1.getvalue('s_id')
def req(q,s_id):
  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
  }

  params = (
    ('q', q),
    ('sessionId', s_id),
  )

  r=requests.get('https://console.dialogflow.com/api-client/demo/embedded/86f65547-dbee-4b4a-ae30-28d6b297f137/demoQuery', headers=headers, params=params).text
  j=json.loads(r)
  print(j['result']['fulfillment']['speech'])
req(q,s_id)

mariadb_connection = mariadb.connect(user='root', password='987', database='db1')
cursor = mariadb_connection.cursor()
mysqlq='INSERT into user_chat(s_id,query) values("'+s_id+'","'+q+'")'
cursor.execute(mysqlq)
mariadb_connection.commit()

