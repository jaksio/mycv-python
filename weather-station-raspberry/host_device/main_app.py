from datetime import datetime
from plotting import run_all as plt
from importing import all_to_html
import time

while True:
    plt()
    all_to_html()
    
    print('done')
    time.sleep(60*4)
