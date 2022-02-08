import serial, time
from time import sleep

ser = serial.Serial('/dev/ttyUSB0')


def read_pm():
    '''read pm25 and pm10 from SDS011 Nova Fitness'''
    data = []
    
    # Take in 10 bytes of data 
    for index in range(0,10):
        data1 = ser.read()
        data.append(data1)
    
    # from bytes read PM25 PM10 and return it in list format
    pm25 = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    pm10 = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    return [pm25, pm10]


if __name__ == "__main__":
    while True:
        print(read_pm())
        sleep(60*5)
