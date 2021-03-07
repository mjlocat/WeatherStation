import sys
import json
import time
from dotenv import DotEnv
import mysql.connector

dotenv = DotEnv()
dbconfig = {
	'user': dotenv.get('DBUSER'),
	'password': dotenv.get('DBPASS'),
	'host': dotenv.get('DBHOST'),
	'database': dotenv.get('DBDATABASE')
}

cnx = mysql.connector.connect(**dbconfig)
cursor = cnx.cursor()
insert_windspeed = "INSERT INTO windspeed (windspeed, ts) VALUES (%(WS)s, %(t)s)"
insert_winddirection = "INSERT INTO winddirection (winddirection, ts) VALUES (%(WD)s, %(t)s)"
insert_temperature = "INSERT INTO temperature (temperature, ts) VALUES (%(T)s, %(t)s)"
insert_humidity = "INSERT INTO humidity (humidity, ts) VALUES (%(H)s, %(t)s)"
insert_rain = "INSERT INTO rain (rain, ts) VALUES (%(RC)s, %(t)s)"

buf = ''
while True:
	try:
		buf += sys.stdin.read(1)
		if (buf.endswith('\n')):
			raw = json.loads(buf[:-1])
			cursor.execute(insert_windspeed, raw["windSpeed"])
			cursor.execute(insert_winddirection, raw["windDirection"])
			cursor.execute(insert_temperature, raw["temperature"])
			cursor.execute(insert_humidity, raw["humidity"])
			cursor.execute(insert_rain, raw["rainCounter"])
			cnx.commit()
			buf = ''
	except KeyboardInterrupt:
		cursor.close()
		cnx.close()
		sys.exit()
