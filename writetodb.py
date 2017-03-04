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
insert = "INSERT INTO readings (ts, windspeed, winddirection, temp, humidity, rain) VALUES (%(ts)s, %(windspeed)s, %(winddirection)s, %(temp)s, %(humidity)s, %(rain)s)"

buf = ''
while True:
	try:
		buf += sys.stdin.read(1)
		if (buf.endswith('\n')):
			raw = json.loads(buf[:-1])
			data = {
				'ts': time.localtime(float(raw["windSpeed"]["t"])),
				'windspeed': raw["windSpeed"]["WS"],
				'winddirection': raw["windDirection"]["WD"],
				'temp': raw["temperature"]["T"],
				'humidity': raw["humidity"]["H"],
				'rain': raw["rainCounter"]["RC"]
			}
			cursor.execute(insert, data)
			cnx.commit()
			buf = ''
	except KeyboardInterrupt:
		cursor.close()
		cnx.close()
		sys.exit()
