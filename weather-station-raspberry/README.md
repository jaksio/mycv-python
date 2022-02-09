# Projekt stacji pogodowej prezentującej wyniki na lokalnej stronie internetowej
# Prezentacja działania projektu została umieszczona w folderze projektu
Stacja pogodowa składa się z dwóch mikrokontrolerów Raspberry z podłączonymi czujnikami temperatury, ciśnienia i wilgotności - BME280. Do jednego z mikrokontrolerów podłączony jest również czujnik pyłów zawieszonych SDS011 Nova Fitness za pomocą konwertera USB-UART. Projekt pozwala na uruchomienie strony internetowej prezentującej w formie tabeli oraz wykresów pomiary temperatury, wilgotności, ciśnienia, PM2.5, PM10 zebrane w ciągu ostatnich 12 godzin. Wykresy zostały wykonane w module plotly z wykorzystaniem DataFrame biblioteki Pandas. Strona internetowa wykonana została w frameworku Flask. 
Aby uruchomić projekt na urządzeniu hosta należy przejść do folderu host_device oraz użyć komend:
>>> python sensor_data.py & <br />
>>> python3 main_app.py & <br />
>>> python3 mqtt_receive.py &<br />
>>> export FLASK_APP=main_internet_page.py<br />
>>> export FLASK_ENV=development<br />
>>> flask run --host=0.0.0.0<br />

Uruchomienie programów wymaga wykorzystania czujników Raspberry Pi z podłączonymi opisanymi wyżej czujnikami oraz zainstalowania wymaganych modułów: plotly, pandas, flask, paho.mqtt.
Na drugim urządzeniu z podłączonym czujnikiem pyłów SDS011 należy uruchomić program<br />
>> python3 sender/mqtt_send.py
