''' Update json files with proper values '''
import json
from bme280_sensor import get_data
from time import sleep
from datetime import datetime, timedelta


def fill_file_with_zeros(path):
    ''' create empty files if there is none '''
    d = {}
    for i in range(1,145):
        d['{}'.format(i)] = ['00:00',0,0,0,0,0]

    with open(path, 'w') as jsonfile:
        json.dump(d, jsonfile, indent=4)
        

def update_file(path, sensor_values):
    ''' update file with json data then move keys '''

    json_data = ''
    json_temp = {}
    with open(path, 'r') as jsonfile:
        json_data = json.load(jsonfile)
    
    del(json_data['1'])
    for i in json_data.keys():
        temp = str(int(i) - 1)
        json_temp['{}'.format(temp)] = json_data['{}'.format(i)]


    json_temp['144'] = sensor_values
    print(json_temp)
    with open(path, 'w') as jsonfile:
        json.dump(json_temp, jsonfile, indent=4)

    

def main():
    
    
    path = 'data/home_bme280.json'
    path2 = 'data/outside.json'

    # #if no data files
    # fill_file_with_zeros(path)
    # fill_file_with_zeros(path2)

    while True:
        now = datetime.now()
        if now.minute % 5 == 0:
            data = get_data()
            with open('data/now_home.json', 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            update_file(path, data)
            sleep(60*3)



if __name__ == '__main__':
    main()
