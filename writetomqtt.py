import sys
import json
import paho.mqtt.client as mqtt

client = mqtt.Client(client_id="wx-producer")
client.connect(sys.argv[1])
client.loop_start()

buf = ''
while True:
  try:
    buf += sys.stdin.read(1)
    if (buf.endswith('\n')):
      raw = json.loads(buf[:-1])
      client.publish("wx/windspeed", json.dumps(raw["windSpeed"]))
      client.publish("wx/winddirection", json.dumps(raw["windDirection"]))
      client.publish("wx/temperature", json.dumps(raw["temperature"]))
      client.publish("wx/humidity", json.dumps(raw["humidity"]))
      client.publish("wx/raincounter", json.dumps(raw["rainCounter"]))
      buf = ''
  except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
    sys.exit()
