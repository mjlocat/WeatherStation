import sys
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect(sys.argv[1])
client.loop_start()

buf = ''
while True:
  try:
    buf += sys.stdin.read(1)
    if (buf.endswith('\n')):
      raw = json.loads(buf[:-1])
      client.publish("wx/windspeed", raw["windSpeed"])
      client.publish("wx/winddirection", raw["windDirection"])
      client.publish("wx/temperature", raw["temperature"])
      client.publish("wx/humidity", raw["humidity"])
      client.publish("wx/raincounter", raw["rainCounter"])
      buf = ''
  except KeyboardInterrupt:
    client.disconnect()
    client.loop_end()
    sys.exit()
