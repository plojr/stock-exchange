import psycopg2
import os

connected = False
conn = None

def get_cursor():
	global connected
	global conn
	if connected is True:
		return conn, conn.cursor()
	conn = psycopg2.connect(
		host='localhost',
		database='postgres',
		user='postgres',
		password=os.environ['POSTGRESQL_PASSWORD']
	)
	connected = True
	return conn, conn.cursor()