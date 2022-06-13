import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT1-'), 
        sg.Spin(['km to mile', 'kg to pounds', 'sec to min'], key='-SPIN1-'), 
        sg.Button('convert', key='-BUTTON1-')
    ],
    [
        sg.Text('Output'), 
        sg.Text('', key='-OUTPUT_TXT-')
    ]
]

window = sg.Window('Converter program', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-BUTTON1-':
        try:
            float(values['-INPUT1-'])
        except:
            window['-OUTPUT_TXT-'].update("Some error occured, please check input data!")
        else:
            if values['-SPIN1-'] == 'km to mile' and float(values['-INPUT1-']) >= 0:
                window['-OUTPUT_TXT-'].update(round(float(values['-INPUT1-']) * 0.6124, 2))
            elif values['-SPIN1-'] == 'kg to pounds' and float(values['-INPUT1-']) >= 0:
                window['-OUTPUT_TXT-'].update(round(float(values['-INPUT1-']) * 2.20462, 2))
            elif values['-SPIN1-'] == 'sec to min' and float(values['-INPUT1-']):
                if float(values['-INPUT1-']) % 60 == 0.0:
                    window['-OUTPUT_TXT-'].update(int(int(values['-INPUT1-']) /60))
                else:
                    window['-OUTPUT_TXT-'].update(round(float(values['-INPUT1-']) /60, 2))
            else:
                window['-OUTPUT_TXT-'].update('Please enter numbers that greater or equal to zero')
        print(values['-INPUT1-'],  values['-SPIN1-'])
window.close()