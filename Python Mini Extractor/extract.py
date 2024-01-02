import PySimpleGUI as sg
from zipextractor import extract_archive
import zipfile

sg.theme('Black')

label1 = sg.Text('Select Archive:')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='archive')

label2 = sg.Text('Select destination directory:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

extract_button = sg.Button('Extract')
output_label = sg.Text(key='output', text_color='cyan')

window = sg.Window('Archive Extractor',
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED:
        break

    try:
        archivepath = values.get('archive')
        dest_dir = values.get('folder')

        if archivepath is not None and dest_dir is not None:
            extract_archive(archivepath, dest_dir)
            window['output'].update(value='Extraction Completed!')
        else:
            window['output'].update(value='Please select both an archive and a destination folder.')
    except zipfile.BadZipFile:
        window['output'].update(value='Invalid ZIP file. Please select a valid ZIP archive.')
    except AttributeError as e:
        window['output'].update(value=f'Error: {e}')

window.close()
