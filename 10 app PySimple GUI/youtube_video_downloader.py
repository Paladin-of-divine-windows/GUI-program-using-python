import PySimpleGUI as sg
from pytube import YouTube
from pathlib import Path

def get_path():
    file_path = sg.popup_get_folder('Save as', no_window=True)
    
    return Path(file_path)

def progress_check(stream, chunk, bytes_remaining):
    progress_amount = 100 - round(bytes_remaining / stream.filesize * 100)
    window['-PROGRESSBAR-'].update(progress_amount)
    
def on_complete(sream, file_path):
    window['-PROGRESSBAR-'].update()

sg.theme('Darkred1')

def run_window(first_screan):
    global window
    if first_screan:
        start_layout = [[
            sg.Input('', key='-INPUT-'),
            sg.Button('submit', key='-SUBMIT-') 
            ]]
        window = sg.Window('Youtube downloader', start_layout)
    else:    
        info_tab = [
            [sg.Text('Title:'), sg.Text('', key='-TITLE-')],
            [sg.Text('Length:'), sg.Text('', key='-LENGTH-')],
            [sg.Text('Views:'), sg.Text('', key='-VIEWS-')],
            [sg.Text('Author:'), sg.Text('', key='-AUTHOR-')],
            [
                sg.Text('Description:'), 
                sg.Multiline('', key='-DESCRIPTION-', size=(40,20), no_scrollbar=True, disabled=True)
            ],
        ]

        download_tab = [
            [sg.Frame('Best Quality', [[sg.Button('Download', key='-BEST-'),sg.Text('', key='-BESTRES-'), sg.Text('',key='-BESTSIZE-')]])],
            [sg.Frame('Worst Quality', [[sg.Button('Download', key='-WORST-'),sg.Text('', key='-WORSTRES-'), sg.Text('',key='-WORSTSIZE-')]])],
            [sg.Frame('Audio', [[sg.Button('Download', key='-AUDIO-'),sg.Text('', key='-AUDIOSIZE-'), sg.Text('',)]])],
            [sg.VPush()],
            [sg.Button('Change wideo', key='-CHANGEWIDEO-')],
            [sg.Progress(100, size=(20,20), expand_x=True, key='-PROGRESSBAR-', bar_color='red')],
        ]

        layout = [[sg.TabGroup([[
            sg.Tab('info', info_tab), sg.Tab('download', download_tab)]])]]

        window = sg.Window('Youtube downloader', layout, finalize= True)

    
# video_link = 'https://www.youtube.com/watch?v=yWp6SXivHBQ&list=LL&index=4'

run_window(True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-SUBMIT-':
        try:
            video_object = YouTube(values['-INPUT-'],on_progress_callback=progress_check, on_complete_callback=on_complete)
            video_object.title
        except Exception as error:
            if 'regex_search' in str(error):
                sg.popup_ok('Please, Insert correct link!', title = 'ERROR')
            elif 'Errno 11001' in str(error):
                sg.popup_ok('Please, check your internet conection', title = 'ERROR')
            else:
                sg.popup_ok('Ups, something going wrong, please try again', title = 'ERROR')
            window.close()
            run_window(True)
        else:
            window.close()
            # Vieo info
            run_window(False)
            window['-TITLE-'].update(video_object.title)
            window['-LENGTH-'].update(f'{round(video_object.length /60 , 2)} minites')
            window['-VIEWS-'].update(video_object.views)
            window['-AUTHOR-'].update(video_object.author)
            window['-DESCRIPTION-'].update(video_object.description)

            #Download
            window['-BESTSIZE-'].update(f'{round(video_object.streams.get_highest_resolution().filesize / 1048576,1)} MB')
            window['-BESTRES-'].update(video_object.streams.get_highest_resolution().resolution)

            window['-WORSTSIZE-'].update(f'{round(video_object.streams.get_lowest_resolution().filesize / 1048576,1)} MB')
            window['-WORSTRES-'].update(video_object.streams.get_lowest_resolution().resolution)

            window['-AUDIOSIZE-'].update(f'{round(video_object.streams.get_audio_only().filesize / 1048576,1)} MB')

    if event == '-BEST-':
        video_object.streams.get_highest_resolution().download(Path(get_path()))
    if event == '-WORST-':
        video_object.streams.get_lowest_resolution().download(Path(get_path())) 
    if event == '-AUDIO-':
        video_object.streams.get_audio_only().download(Path(get_path()))

    if event == '-CHANGEWIDEO-':
        window.close()
        run_window(True)

window.close()