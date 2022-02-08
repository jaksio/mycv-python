import paho.mqtt.publish as publish
import time
from datetime import datetime
from random import randint
from sds_sensor import read_pm
from bme280_sensor import get_data
import json

# Private ip adress of targetet device to send data via MQTT
MQTT_SERVER = "192.168.43.84"
# MQTT topic of this message
MQTT_PATH = "sensor/data/"

  
def main():
    ''' Function is responsible for continously sending data to MQTT broker '''  
    while True:
        data = []
        now = datetime.now()
        if now.minute % 5 == 0:
            # Every 5 minutes try to send data
            # Preparing data to json format 
            data = get_data()
            data_sds = read_pm()
            data = data + data_sds
            data = json.dumps(data)

            try:
                publish.single(MQTT_PATH, data, hostname=MQTT_SERVER)
                time.sleep(4*60)
            except OSError:
                # If no Wi-Fi on Rasp 
                print("Brak polaczenia z siecia wi-fi")

if __name__ == "__main__":
    main()