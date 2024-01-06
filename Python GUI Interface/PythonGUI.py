import function
import PySimpleGUI as sg
import time
import os

# If the todos.txt file DOES NOT EXIST:
if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('Black')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
# This is the values that is filled up by the users
input_box = sg.InputText(tooltip='Enter todo', key="todo")
# This is the Add labels that was created on the sg.Button('Add')
# You can use the size properties to change it
# mouseover_colors is the color when you hover your mouse cursor over the button
# The key 'Add' is match to the code below for the match event which is 'Add'
add_button = sg.Button('Add', size=10, mouseover_colors='Grey')

# This is the list_box for the different various items that is added
list_box = sg.Listbox(values=function.get_todos(), key='todos',
                      # Size of the Box
                      # This is the width and the height(width, height)
                      # of the widget list_box
                      enable_events=True, size=[45, 10])

edit_button = sg.Button('Edit', mouseover_colors='LightBlue')

complete_button = sg.Button('Complete', mouseover_colors='Blue')

exit_button = sg.Button('Exit', mouseover_colors='Green')

# Each List inside actually represent the Row
window = sg.Window('My To-Do-Application',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   # This is the font family and font-Size
                   font=('Helvetica', 20))

# This will keep the Window Open using the Boolean True

while True:
    # The event here is the 'Add' Button
    # values here is the key="todos" and value pairs
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # 1
    # todos

    # 2
    # {'todo': '', 'todos': ['Add todo1\n']}

    # 3
    # ['Add todo1\n']

    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    # x,y=(3,4)
    # x will get values of 3.
    # y will get values of 4.
    # Extracting the key here to get the values with the key-values Pair

    # ('Add', {'todo': 'add'})

    # This match event is matching to the 'Add' or 'Edit'
    if event == "Add":
        # Invoke the get_todos() in the function module
        # This is the read ('r') function
        todos = function.get_todos()
        # This function will read the current items before the users added new items

        # We get the 'Hi' values here
        # This give us the values of the todo key in the input box
        # The values['todo'] is what the user input into the code
        # '/n' is to add a break lines afterward.
        new_todo = values['todo'] + '\n'
        # This function will read the current items that is being added to the list
        print(new_todo)

        # The todos is in a List, Hence, you will need to use append method
        todos.append(new_todo)

        # Using the write_todos here
        function.write_todos(todos)

        # Updating in real time
        # We point to the list box instance, we point to the Method Update
        # values=todos which is the updated (values=todos).
        # values=function.get_todos()
        # This will update to the Edit screen in real time
        window['todos'].update(values=todos)

    elif event == "Edit":
        try:
            # This is the todo to edit of that particular string, you are selecting the
            # key here to get the values for the key-value pair
            todo_to_edit = values['todos'][0]

            # This is the new todo which the users input and you will add the + '/n' to
            # add the break-line after that
            new_todo = values['todo'] + '\n'

            # Reading the current todos list
            todos = function.get_todos()
            # We get the index of the todo to edit
            index = todos.index(todo_to_edit)
            # This is the updated new_todo which the
            # user input and replace the current todos[index]
            todos[index] = new_todo
            # writing it to the todos.txt
            function.write_todos(todos)
            # Updating it in real time
            # values=function.get_todos()
            # values here is the lists of the items
            # You are getting the updated todos
            window['todos'].update(values=todos)

        except IndexError:
            sg.popup('Please select an item first.', font=("Helvetica", 20))

    elif event == 'todos':  # window['todo'] is the input text box
        # update is the method for the window object
        # the values['todos'] here refer to the key itself
        # values['todos'][0] will extract the string
        # window['todo'] is the input box.
        # the window['todo'] refer to the input box
        # Hence you want to update the input box value to be equal
        # to the value=values['todos'][0]
        window['todo'].update(value=values['todos'][0])

    elif event == 'Complete':
        try:
            todo_to_complete = values['todos'][0]
            todos = function.get_todos()
            todos.remove(todo_to_complete)
            # function.write_todos(todos) need an argument
            # Look at the code in the function.py
            function.write_todos(todos)
            # values here is the lists of the items
            # The todos here is the updated todos after an item has been removed
            window['todos'].update(values=todos)
            # Updating the window['todo'] to be empty string which represent nothing
            window['todo'].update(value='')
        except IndexError:
            sg.popup('Please select an item first', font=('Helvetica', 20))
    # Prevent the while Loop from executing by itself using the break statement:

    elif event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()

# How the code work:
# When the Python GUI Application is open
# You can add the todos, edit the todos or complete the todos.
# Add the todos in the input box, and this will be added in the input box.
# You can also edit the todos, editing the todos will basically allow
# you to change the values inside the todos itself.
# Complete the todos will remove the todos completely.

