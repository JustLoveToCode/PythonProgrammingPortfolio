import tkinter as tk
from tkinter import ttk

def convert_miles_to_kilometers():
    try:
        miles = float(entry.get())
        kilometers = miles * 1.60934
        output_label.config(text=f'{miles} miles is {kilometers:.2f} kilometers')
    except ValueError:
        output_label.config(text='Invalid input. Please enter a valid number.')

# Window
window = tk.Tk()
window.title('Demo Converter')
window.geometry('550x250')

# title
title_label = ttk.Label(master=window, text='Convert the Miles to the Kilometers', font='Calibri 24 bold')
title_label.pack()

# Input Field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='Convert Here!', command=convert_miles_to_kilometers)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=20)

# Output
output_label = ttk.Label(master=window, text='Output Here', font='Calibri 25 bold')
output_label.pack(pady=5)

# Run the Main Loop
window.mainloop()
