import tkinter
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import random

# Instantiating the object  for the Tkinter Application:
root = Tk()
# Instantiating the style object:
style = ttk.Style()

# Instantiating the ThemedStyle object for the OptionMenu:
style_1 = ThemedStyle(root)

# Setting the Title for the Music Player Playlist:
root.title('Music_Player Playlist')
# Setting the Background to be black:
root.configure(background='black')
# Setting the Geometry of the Screen:
root.geometry('1000x800')

# Opening the Image:
# Set the Path of your Image to be in the Root Application of Python:
# It can be Image.jpg or anything
image = Image.open("Image.jpg")

# Convert the Image into PhotoImage:
# PhotoImage is the Image Format for the Tkinter Label Widget
# Tkinter Widget is designed to work with the PhotoImage Objects
# for displaying the Images:
# Tkinter and Pillow are the Separate Libraries, so they have their
# Own Image Format. Converting the image to the PhotoImage integrate your
# images into the Tkinter Interface:
image = ImageTk.PhotoImage(image)


# Create a label to display the image
# Stacking Order of the Widgets allowed it to appear in the Background:
# First widget appear in the Background Always
# relwidth: Value between 0 and 1, 1 represent the full width of the parent container
# relheight: Value between 0 and 1, 1 represent the full height of the parent container
# root is the Parent Container here. relwidth and relheight refer back to the root
background_label = Label(root, image=image)
background_label.place(relwidth=1, relheight=1)

title_label = Label(root, text='Music Player Application', font=('Calibre', 20, 'bold'))
title_label.grid(row=3, column=1, padx=10, pady=(20, 0))

# Initiate Pygame Mixer Module:
mixer.init()

# Creating the Label Frame which is the Container
style.configure('Custom.TLabelframe', background='cyan')
style.configure('Custom.TLabelframe.Label', background='LightBlue', foreground='black', font=('Calibre', 16, 'bold'))

# Configure the Appearance of the Listbox
style.configure('Custom.TListbox', background='cyan', foreground='black', font=('Calibre', 12))

# Create the LabelFrame with the Custom Style
labelframe = ttk.LabelFrame(root, text="Song Playlist Here", style='Custom.TLabelframe', width=10, height=10)
labelframe.grid(row=0, column=1, padx=10, pady=(20, 0))

# Creating the Listbox that is placed inside the LabelFrame
# defining the width=50 and height=10 for the listbox.
playlist_listbox = Listbox(labelframe, width=50, height=10, bg='white', fg='black', font=('Calibre', 12))
playlist_listbox.grid(row=0, column=1, padx=10, pady=(20, 0))

# Declaring the Empty List:
selected_files = []


# Defining the Open file
def open_file():
    # Get the selected file path by selecting 1 single file:
    file_path = filedialog.askopenfilename(filetypes=[('All Files', '*.*')])
    if file_path:
        # Extract the file name from the path
        file_name = file_path.split("/")[-1]
        # Insert the file_name into the Listbox widget,
        # End: items is inserted at the end of the Listbox widget
        playlist_listbox.insert(END, file_name)
        # Using the append method to append to the array
        selected_files.append(file_name)


# Defining the Remove file from the Listbox
def remove_file():
    # Get the Index of the Selected Item
    selection = playlist_listbox.curselection()
    # If selection exist
    if selection:
        index = selection[0]
        # remove the selected item from the listbox visually
        playlist_listbox.delete(index)
        # remove the selected item from the selected_files array
        selected_files.pop(index)


# Defining the Edit file from the Listbox
def edit_file():
    # Get the Index of the Selected Item
    selection = playlist_listbox.curselection()
    # If selection exist
    if selection:
        index = selection[0]
        file_path = filedialog.askopenfilename(filetypes=[('All Files', '*.*')])
        # If file_path exist
        if file_path:
            # Split the filepath into its individual Array Items
            # and take the last items using -1
            file_name = file_path.split("/")[-1]
            # delete the file for that particular index
            playlist_listbox.delete(index)
            # Insert the given element at a given index into the Array
            playlist_listbox.insert(index, file_name)
            selected_files[index] = file_path


# Defining the play function
def play():
    # Getting the file_path from the selected_files in the List
    file_path = random.choice(selected_files)
    mixer.music.load(file_path)
    mixer.music.play()
    update_slider(file_path)


# Defining the stop function
def stop():
    mixer.music.pause()


# Defining the resume function
def resume():
    mixer.music.unpause()


# Defining the set_volume function
def set_volume(vol):
    volume = int(vol) / 100
    mixer.music.set_volume(volume)


def update_slider(file_path):
    # Initializing the Object that represent the MP3 Audio file
    # Object allowed you to extract information about the Audio files,
    # such as the Duration, artists, title, album.
    audio = MP3(file_path)
    # This will give you the duration of the Entire MP3
    song_length = audio.info.length
    # Get the Current Position in Seconds
    current_position = mixer.music.get_pos()
    # Calculate the Percentage Position of the Slider
    position_percentage = (current_position / (song_length * 1000)) * 100
    # Update Position Slider
    position_slider.set(position_percentage)


# Defining the slider:
def slider(value):
    position_percentage = float(value)
    song_length = 0

    # This will only be True if the Music Player is actually playing
    if mixer.music.get_busy():
        # Getting the Music Player that is currently played
        file_path = random.choice(selected_files)
        # Initializing the Object that represents the MP3 Audio file
        audio = MP3(file_path)
        # This will give you the duration of the Entire MP3 in seconds
        song_length = audio.info.length

    position_seconds = (position_percentage / 100) * song_length

    mixer.music.set_pos(position_seconds)
    position_slider.set(position_percentage)


# Default mode of repeat_mode
repeat_mode = StringVar(value="None")


# Defining the repeat Function
def repeat(option):
    if option == 'None':
        mixer.music.stop()
    elif option == 'Once':
        mixer.music.play(1)
    elif option == 'Indefinitely':
        mixer.music.play(-1)


def fast_forward():
    if mixer.music.get_busy():
        current_position = mixer.music.get_pos() / 1000
        file_path = random.choice(selected_files)
        audio = MP3(file_path)
        song_length = audio.info.length
        new_position = current_position + 10
        mixer.music.set_pos(new_position)
        position_slider.set((new_position / song_length) * 100)


def fast_backward():
    if mixer.music.get_busy():
        current_position = mixer.music.get_pos() / 1000
        file_path = random.choice(selected_files)
        audio = MP3(file_path)
        song_length = audio.info.length
        new_position = current_position - 10
        mixer.music.set_pos(new_position)
        position_slider.set((new_position / song_length) * 100)


# Position Label:
position_label = Label(root, text='Position Slider', font=('Calibre', 20, 'bold'))
position_label.grid(row=0, column=0, padx=10, pady=(20, 0))

# Position Slider:
position_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=slider,
                        background='white', troughcolor='gray', sliderlength=50,
                        bd=0, highlightthickness=0, length=240,
                        showvalue=False)
position_slider.set(20)
position_slider.grid(row=1, column=0, padx=10, pady=(0, 20))

# Volume Slider
volume_label = Label(root, text='Volume Slider', font=('Calibre', 20, 'bold'))
volume_label.grid(row=0, column=2, padx=10, pady=(20, 0))

volume_slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_volume,
                      background='white', troughcolor='gray', sliderlength=50,
                      bd=0, highlightthickness=0, length=240,
                      showvalue=False)
volume_slider.set(20)
volume_slider.grid(row=1, column=2, padx=10, pady=(0, 20))

# Styling the Shuffle Button:
style.configure('Shuffle.TButton', background='blue', foreground='black', font=('Calibre', 12, 'bold'), padding=10)
style.map('Shuffle.TButton', background=[('active', 'blue')])

# Adding the Shuffle Button:
shuffle_button = ttk.Button(root, text="Shuffle Button", command=play, style='Shuffle.TButton')
shuffle_button.grid(row=7, column=2, padx=10, pady=(20, 0))

# Styling the Remove Button:
style.configure('Remove.TButton', background='blue', foreground='brown', font=('Calibre', 12, 'bold'), padding=10)
style.map('Remove.TButton', background=[('active', 'gold')])

# Adding the Remove Button:
remove_button = ttk.Button(root, text="Remove Button", command=remove_file, style='Edit.TButton')
remove_button.grid(row=5, column=2, padx=10, pady=(20, 0))

# Styling the Edit Button:
style.configure('Edit.TButton', background='blue', foreground='brown', font=('Calibre', 12, 'bold'), padding=10)
style.map('Edit.TButton', background=[('active', 'gold')])

# Adding the Edit Button
edit_button = ttk.Button(root, text="Edit Button", command=edit_file, style='Edit.TButton')
edit_button.grid(row=5, column=1, padx=10, pady=(20, 0))

# Styling the Fast Forward Button:
style.configure('FastForward.TButton', background='orange', foreground='black', font=('Calibre', 12, 'bold'),
                padding=10)
style.map('FastForward.TButton', background=[('active', 'orange')])

# Fast Forward Button:
fast_forward_button = ttk.Button(root, text="Fast Forward", command=fast_forward, style='FastForward.TButton')
fast_forward_button.grid(row=6, column=0, padx=10, pady=(20, 0))

# Style the Fast-Backward Button:
style.configure('FastBackWard.TButton', background='cyan', foreground='black', font=('Calibre', 12, 'bold'), padding=10)
style.map('FastBackWard.TButton', background=[('active', 'cyan')])

# Fast-Backward Button:
fast_backward_button = ttk.Button(root, text="Fast BackWard", command=fast_backward, style='FastBackWard.TButton')
fast_backward_button.grid(row=7, column=0, padx=10, pady=(20, 0))

# Styling the Browse Button:
style.configure('Browse.TButton', background='blue', foreground='black', font=('Calibre', 12, 'bold'), padding=10)
style.map('Browse.TButton', background=[('active', 'blue')])

# Adding the Browse Button:
browse_button = ttk.Button(root, text="Browse Button", command=open_file, style='Browse.TButton')
browse_button.grid(row=5, column=0, padx=10, pady=(20, 0))

# Styling the Play Button:
style.configure('Play.TButton', background='purple', foreground='black', font=('Calibre', 12, 'bold'), padding=10)
style.map('Play.TButton', background=[('active', 'purple')])

# Adding the Play Button:
play_button = ttk.Button(root, text="Play Button", command=play, style='Play.TButton')
play_button.grid(row=7, column=1, padx=10, pady=(20, 0))

# Styling the Pause Button:
style.configure('Pause.TButton', background='cyan', foreground='black', font=('Calibre', 12, 'bold'), padding=10)
style.map('Pause.TButton', background=[('active', 'cyan')])

# Adding the Pause Button:
pause_button = ttk.Button(root, text="Pause Button", command=stop, style='Pause.TButton')
pause_button.grid(row=6, column=1, padx=5, pady=(20, 0))

# Styling the Resume Button:
style.configure('Stop.TButton', background='yellow', foreground='black', font=('Calibre', 12, 'bold'), padding=10)
style.map('Stop.TButton', background=[('active', 'yellow')])

# Adding the Resume Button:
resume_button = ttk.Button(root, text="Resume Button", command=resume, style='Stop.TButton')
resume_button.grid(row=6, column=2, padx=10, pady=(20, 0))

# Styling the Repeat Button OptionMenu:
style_1.configure('CustomOption.TMenubutton', font=('Calibre', 20))

# Adding the Repeat Button OptionMenu:
repeat_button = ttk.OptionMenu(root, repeat_mode, "None", "Once", "Indefinitely", command=repeat,
                               style='CustomOption.TMenubutton')
repeat_button.grid(row=3, column=2, padx=10, pady=(20, 0))

root.mainloop()



