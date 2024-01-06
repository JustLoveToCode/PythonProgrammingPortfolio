FILEPATH = 'todos.txt'


def get_todos(filepath='todos.txt'):
    """Read a text file and return the list of
    to-do items
    """

    with open(filepath, 'r') as file_local:
        # The program will read it lines by lines
        # and return it as the List of the Strings ['a','b','c'] here:
        # ['Buy groceries\n', 'Complete assignment\n', 'Go for a run\n']
        todos_local = file_local.readlines()
    # After the Computer has read the lines using the readlines() code
    # return todos_local
    return todos_local


# The Non-default parameter need to be written first, followed by Default Parameter
# todos_arg is always changing, hence, it does not have a default parameter

""" Write the to-do items 
list in the text file """


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do
    items list in the text file
    """

    with open(filepath, 'w') as file:
        for todo in todos_arg:
            file.writelines(todo)


def delete_todo():
    try:
        number = int(input('Enter the number for the Todo to delete: '))
        todos = get_todos()

        if 1 <= number <= len(todos):
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list,"
            print(message)
        else:
            print("Invalid todo number. Please enter a valid number.")
    except ValueError:
        print('Invalid input. Please enter a valid number.')


# This will give you the '__main__' output

if __name__ == '__main__':
    print('Hello')
    # This will write or read the file in the
    # def get_todos(filepath = 'todos.txt')
    print(get_todos())
