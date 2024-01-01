import PySimpleGUI as sg


def km_to_miles(km):
    return km / 1.6

# Creating the Graphical User Interface(GUI):
label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")


window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    # Using if, elif, and else for event handling
    if event == "Convert":
        km = float(values["kms"])
        result = km_to_miles(km)
        window['output'].update(value=result)
    elif event == sg.WIN_CLOSED:
        break

window.close()


