import psycopg2
import os

connected = False
conn = None

def get_connection():
	global connected
	global conn
	if connected is True:
		return conn, conn.cursor()
	conn = psycopg2.connect(
		host = "localhost",
		database = os.environ["POSTGRESQL_DATABASE"],
		user = os.environ["POSTGRESQL_USER"],
		password = os.environ["POSTGRESQL_PASSWORD"],
		options='-c search_path=stock_exchange'
	)
	connected = True
	return conn, conn.cursor()
