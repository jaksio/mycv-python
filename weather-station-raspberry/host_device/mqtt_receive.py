''' Module implements paho mqtt broker '''
import paho.mqtt.client as mqtt
from sensor_data import update_file
from io import StringIO
import json
import ast

# This is broker so mqtt server is localhost
MQTT_SERVER = "localhost"
# topic of mqtt
MQTT_PATH = "sensor/data/"

# The callback for when the client receives a connect response from the server.
def on_connect(client, userdata, flags, rc):
    ''' print statement after successfull connection '''
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_PATH)


def on_message(client, userdata, msg):
    ''' Do this after receiving MQTT message '''
    path = 'data/outside.json'
    data = msg.payload.decode("utf-8", "ignore")
    data = json.loads(data)
    with open('data/now_out.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)
    update_file(path, data)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()