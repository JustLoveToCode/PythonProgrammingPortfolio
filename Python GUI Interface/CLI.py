# import get_todos and write_todos:
from function import get_todos, write_todos, delete_todo
import time

# Input the time and date:
now = time.strftime("%d %b %Y, %H:%M:%S")
print("It is ", now)

while True:
    user_action = input('Type add or show or edit or exit or complete or delete: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        # add todo1: take the 4th index which is from t onward:
        todo = user_action[4:]

        # This is the function calls to Invoke the function
        # This is a Global Variable
        # This is like the Function Parameter
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        # new_todos=[item.strip('/n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('delete'):
        delete_todo()

    elif user_action.startswith('edit'):
        try:
            # user_action here is in string, hence you need to convert
            # this into integer from string. string to integer conversion
            number = int(user_action[5:])
            # User Experience: Minus 1 to get the Index of 1.
            number = number - 1

            todos = get_todos()

            new_todo = input('Enter New todos:')

            todos[number] = new_todo + '\n'

            # Only for this todos arg then you will need to
            # define it, because it is always changing
            write_todos(todos)

        # Important to Specify the Error which is the ValueError:
        except ValueError:
            print('Your Command is not Valid, Please Enter the Command again')
            # continue statement will run the while loop
            # It will ignore everything that goes underneath and will go back
            # to the beginning of the code
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list,"

            print(message)
        except (IndexError, ValueError):
            print("There is no item with that Number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Command is not VALID')

print('Bye, We hope to see you again')
