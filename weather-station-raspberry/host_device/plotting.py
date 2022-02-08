''' Module plotting charts with data to html output files '''
import io
from base64 import b64encode
import json
import plotly
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta


def datetime_range(start, end, delta):
    ''' datetime range function '''
    current = start
    while current < end:
        yield current
        current += delta

def load_data(path):
    ''' load data from json and load it to python dictionary '''
    jsondata = ''
    with open(path, 'r') as jsonfile:
        for i in jsonfile:
            jsondata += i

    dict_json = json.loads(jsondata)
    return dict_json

def prepare_data_frame(
    dictionary: dict, val_position: int, val_name: str):
    ''' returns pandas prepared DataFrame for plotting '''
    time = []
    val = []
    
    keys_list = [int(i) for i in dictionary.keys()]
    keys_list = sorted(keys_list)
    
    # Depends on chosen value (temperature, humidity etc)
    for key in keys_list:
        time.append(dictionary[str(key)][0])
        val.append(dictionary[str(key)][val_position])
     
    dictionary = {'godzina': time, val_name: val}
    dictionary = pd.DataFrame(data=dictionary)
    return dictionary


def draw_plot(
        dictionary: dict, file_name: str,
        val_pos: int, val_name: str, title: str):
    ''' takes prepared by pandas dataframe and draws chart with plotly '''
    df = prepare_data_frame(dictionary, val_pos, val_name)
    
    fig = px.line(df, x = 'godzina',
                  y = val_name,
                  title=title)
    

    dts = [dt.strftime('%H:%M') for dt in
              datetime_range(
                datetime.strptime(str(dictionary['144'][0]),'%H:%M')- timedelta(hours=12,minutes=5),
                datetime.strptime(str(dictionary['144'][0]),'%H:%M'),
                timedelta(minutes=15))
           ]
    
    fig.update_xaxes(tickvals=dts)
    
    fig.update_layout(autotypenumbers='convert types')
    file_name = 'templates/' + file_name + '.html'
    
    plotly.offline.plot(
            fig, filename = file_name,
            auto_open=False)


def run_all():
    ''' Runs all drawing and saving to files, next run importing module to place 2 charts in one html file '''
    path = 'data/home_bme280.json'
    path2 = 'data/outside.json'
    dict_json = load_data(path)
    dict_json1 = load_data(path2)
    
    draw_plot(
        dict_json, 'temperatury', 1,
        'Stopnie Celsjusza', 'Wykres temperatury w pokoju')
    draw_plot(
        dict_json, 'wilgotnosci', 2,
        'Wilgotnosc w procentach', 'Wykres wilgotnosci w pokoju')
    draw_plot(
        dict_json, 'cisnienia', 3,
        'hPa', 'Wykres cisnienia w pokoju')
    
    draw_plot(
        dict_json1, 'temperatury1', 1,
        'Stopnie Celsjusza', 'Wykres temperatury na zewnątrz')
    draw_plot(
        dict_json1, 'wilgotnosci1', 2,
        'Wilgotnosc w procentach', 'Wykres wilgotnosci na zewnątrz')
    draw_plot(
        dict_json1, 'cisnienia1', 3,
        'hPa', 'Wykres cisnienia na zewnątrz')
    draw_plot(
        dict_json1, 'pm25', 4,
        'μg/m3', 'Wykres pm2.5')
    draw_plot(
        dict_json1, 'pm10', 5,
        'μg/m3', 'Wykres pm10')

    


def main():
    run_all()

if __name__ == '__main__':
    main()
