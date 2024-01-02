import PySimpleGUI as sg
# BackEnd Development, importing the zipCreator
from zipCreator import make_archive

label1 = sg.Text('Select files to compress:')
input1 = sg.Input()
# This is the files that you choose from your desktop
choose_button1 = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text('Select Destination Folder:')
input2 = sg.Input()
# This is the Folder Destination, which is the text that is shown on the button
choose_button2 = sg.FolderBrowse('Choose', key='folder')

compress_button = sg.Button('Compress')
output_label = sg.Text(key="output")

window = sg.Window('File Compressor', layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!", text_color='cyan')

window.close()
