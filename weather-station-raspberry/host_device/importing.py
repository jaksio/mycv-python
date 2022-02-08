''' This module prepares html file for the website pages with two plots done in plotly and saved in html files '''
import json


# Prepare strings 
start_html = '{' + chr(37) + 'extends "layout.html"' + chr(37) + '}{' 
start_html += chr(37) + 'block content ' + chr(37) 
start_html += '}<div class="header"><h1>Wykres'

middle_html = '</h1></div>'
end_html = '{' + chr(37) + 'endblock content ' + chr(37) + '}'

button = '''<button class="button" onclick="window.location.href='{{ url_for('home') }}'"><span>Strona główna</span></button>'''


def get_html_body(input_f: str) -> str:
    '''gets html file name and returns only body of that file'''
    
    html = []
    string_html= ''
    file = 'templates/' + input_f
    
    
    with open(file, 'r') as htmlfile:
            html = htmlfile.readlines()
            
    for i in html[2:62]:
        string_html += i
    
    return string_html
    

def save_two_plot(in_file: str) -> None:
    ''' depending if first plot or second one places string in right place in html '''
    
    plot_file = 'templates/wykres_' + in_file
    first_f_str = get_html_body(in_file)
    second_file = in_file[0:-5] + '1.html'
    second_f_str = get_html_body(second_file)
    
    full_str = start_html.join(' ', middle_html, first_f_str, second_f_str, button, end_html) # + ' ' + in_file[0:-5] + middle_html + first_f_str + second_f_str + button + end_html


    with open(plot_file, 'w') as htmlfile:
            htmlfile.write(full_str)


def save_pm_plot(in_file: str) -> None:
    plot_file = 'templates/wykres_' + in_file
    first_f_str = get_html_body(in_file)
    
    full_str = start_html.join(' ', in_file[0:-5], middle_html, first_f_str, button, end_html) # + ' ' + in_file[0:-5] + middle_html + first_f_str + button + end_html


    with open(plot_file, 'w') as htmlfile:
            htmlfile.write(full_str)
    
    
def all_to_html():
    save_two_plot('temperatury.html')
    save_two_plot('wilgotnosci.html')
    save_two_plot('cisnienia.html')
    
    save_pm_plot('pm25.html')
    save_pm_plot('pm10.html')
    
    
def main():
    all_to_html()
    

if __name__ == '__main__':
    main()