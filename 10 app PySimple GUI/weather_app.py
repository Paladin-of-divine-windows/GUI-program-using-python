import PySimpleGUI as sg
import os 
from bs4 import BeautifulSoup as bs 
import requests


def get_wether_data(location):
    url =f"https://www.google.com/search?client=firefox-b-d&q=weather+{location.replace(' ','')}"
    session = requests.Session()
    session.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    html = session.get(url)

    soup = bs(html.text, 'html.parser')
    name = soup.find('div', attrs={'id':'wob_loc'}).text
    time = soup.find('div', attrs={'id':'wob_dts'}).text
    weather = soup.find('span', attrs={'id':'wob_dc'}).text
    temp = soup.find('span', attrs={'id':'wob_tm'}).text 
    return name, time, weather, temp

sg.theme('reddit')
dir_path = os.path.dirname(os.path.realpath(__file__))
image_col = sg.Column([[sg.Image(key='-IMAGE-', background_color='#FFFFFF', visible=False)]])
info_col = sg.Column([
    [sg.Text('', key='-LOCATION-', font='Calibri 30', background_color='#FF0000', text_color='#FFFFFF', pad = 0, visible=False)],
    [sg.Text('', key='-TIME-', font='Calibri 16', background_color='#000000', text_color='#FFFFFF', pad=0, visible=False)],
    [sg.Text('', key='-TEMP-', font='Calibri 16', background_color='#FFFFFF', text_color='#000000', pad=(0,10), visible=False, justification='center')],
])
layout = [
    [sg.Input(expand_x=True, key= '-INPUT-'), sg.Button('Enter', button_color='#000000', border_width='0')],
    [image_col, info_col],
    ]

window = sg.Window('Weather', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Enter':
        name, time, weather, temp = get_wether_data(values['-INPUT-'])
        window['-LOCATION-'].update(name, visible= True)
        window['-TIME-'].update(time.split(' ')[0], visible= True)
        window['-TEMP-'].update(f'{temp} \u2103 ({weather})' , visible= True)
        if weather in ('Сонячно'):
            window['-IMAGE-'].update(str(dir_path)+'/symbols/sun.png', visible = True)
        else:
            window['-IMAGE-'].update(str(dir_path)+'/symbols/cloud.png', visible = True)
        
window.close()