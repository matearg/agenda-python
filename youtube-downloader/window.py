import PySimpleGUI as sg
from pytube import YouTube

sg. theme('Darkred1')

start_layout = [[sg.Input(key = '-INPUT-'), sg.Button('Submit')]]

info_tab = [
    [sg.Text('Title:'), sg.Text('', key = '-TITLE-')],
    [sg.Text('Length:'), sg.Text('', key = '-LENGTH-')],
    [sg.Text('Views:'), sg.Text('', key = '-VIEWS-')],
    [sg.Text('Author:'), sg.Text('', key = '-AUTHOR-')],
    [
        sg.Text('Description'),
        sg.Multiline('', key = '-DESCRIPTION-', size = (40,20), no_scrollbar = True, disabled = True)
    ]
]

download_tab = [
    [sg.Frame('Best quality', [[sg.Button('Download', key = '-BEST-'), sg.Text('', key = '-BESTRES-'), sg.Text('', key = '-MEJORTAMANIO-')]])],
    [sg.Frame('Worst quality', [[sg.Button('Download', key = '-WORST-'), sg.Text('', key = '-WORSTRES-'), sg.Text('', key = '-PEORTAMANIO-')]])],
    [sg.Frame('Audio', [[sg.Button('Download', key = '-AUDIO-'), sg.Text('', key = '-AUDIORES-')]])],
    [sg.VPush()],
    [sg.Progress(100, size = (20,20), expand_x = True, key = '-PROGRESSBAR-')]
]

layout = [[sg.TabGroup([[
    sg.Tab('Info',info_tab), sg.Tab('Download',download_tab)
    ]])]]

window = sg.Window('Youtube Downloader', start_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        video_object = YouTube(values['-INPUT-'])
        window.close()

        window = sg.Window('Youtube Downloader', layout, finalize = True)
        window['-TITLE-'].update(video_object.title)
        window['-LENGTH-'].update(f'{round(video_object.length / 60.2)} minutes')
        window['-VIEWS-'].update(video_object.views)
        window['-AUTHOR-'].update(video_object.author)
        window['-DESCRIPTION-'].update(video_object.description)

window.close()
