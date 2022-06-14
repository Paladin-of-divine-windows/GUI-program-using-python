import PySimpleGUI as sg
from pathlib import Path

smileys = ['happy',[':)', 'xD', ':D', '<3'],
        'sad', [':(', 'T_T'],
        'other', [';3']]
smiley_event = smileys[1] + smileys[3] + smileys[5]

manu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word count']],
    ['Add', smileys],
    ]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(manu_layout)],
    [sg.Text('Untitled', key='-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size=(40,30), key='-TEXTBOX-')],
    ]

window = sg.Window('Text_editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Open':
        file_path = sg.popup_get_file('open', no_window=True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(file_path.split('/')[-1])
    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as=True) + '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Word count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        Word_count = 0
        for i in clean_text:
            if len(i) > 0:
                Word_count += 1
        char_count = len(''.join(clean_text))
        sg.Popup(f'words {Word_count}\ncharacters {char_count}')

    if event in smiley_event:
        full_text = values['-TEXTBOX-'] +  ' ' + event
        window['-TEXTBOX-'].update(full_text)
window.close()