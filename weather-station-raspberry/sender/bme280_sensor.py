''' Module responsible for getting data from bme280 sensor '''
import bme280
import smbus2
from time import sleep
from datetime import datetime

port = 1
address = 0x77
bus = smbus2.SMBus(port)

params = bme280.load_calibration_params(bus, address)

def get_data(address=address, bus=bus, params=params):
    ''' gets data from bme280 sample and returns it in list format with time in hour:minute '''
    mySensor = bme280.sample(bus, address, params)
    humidity = round(mySensor.humidity, 1)
    pressure = round(mySensor.pressure, 1)
    temperature = round(mySensor.temperature, 1)
    now = datetime.now().strftime("%H:%M")
    return [now, temperature, humidity, pressure]

if __name__ == '__main__':
    while True:
        print(get_data())
        sleep(60*5)