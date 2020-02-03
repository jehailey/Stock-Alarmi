##############################
# Reguirement 
# Python 3
############################

import psycopg2
import sys

# Change the variables accordingly
localhost = "localhost"
port = 22222
dbname = sys.argv[1]
user = "postgres"
password = "jehailey"


def create_tables(conn, cur):
	create_candlestick_table = """CREATE TABLE IF NOT EXISTS Candlestick (
			SYMBOL CHAR(10) PRIMARY KEY     NOT NULL,
			TIMESTAMP TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
			LOW DECIMAL(12, 6)    NOT NULL,
			HIGH DECIMAL(12, 6)    NOT NULL,
			OPEN DECIMAL(12, 6)    NOT NULL,
			CLOSE DECIMAL(12, 6)    NOT NULL,
			VOLUME DECIMAL(12, 6)    NOT NULL)"""
    
	cur.execute(create_candlestick_table)
	conn.commit()


def update_table(conn, cur):
	pass

def run():
	try:
		# create DB connection
		conn = psycopg2.connect(
		    host=localhost,
		    port=port,
		    database=dbname,
		    user=user,
		    password=password
		)
		cur = conn.cursor()

		# run to create tables
		create_tables(conn, cur)

		# run to update the tables
		# update_table(conn, cur)

		# run to retrieve data from the tables

	except(Exception, psycopg2.DatabaseError) as error:
		print(" Error connecting to the database table", error)

	finally:
		if(conn):
			print(" Successfully completed the query")
			cur.close()
			conn.close()

# run the script
run()
