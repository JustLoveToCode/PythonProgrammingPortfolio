import turtle
import pandas

def get_mouse_click(x, y):
    print(x, y)

# Creating the screen object:
screen = turtle.Screen()
# Setting the .gif to the variable image:
image = "blank_states_img.gif"
screen.addshape(image)
# Setting the title of the screen object:
screen.title("US States Game")
turtle.shape(image)
# Invoking the get_mouse_click function:
turtle.onscreenclick(get_mouse_click)

# Read the Data and Convert it into the DataFrame:
data = pandas.read_csv("50_states.csv")
# Convert it into the List of Items using the to_list():
all_states = data.state.to_list()
# Creating the Empty List:
guessed_states = []

# Using the while keyword:
# len which will give you the length of the List:
# The len keyword will give you the length of the List:
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State: {len(guessed_states)} Correct", prompt="What is the State Name?")
    # Using the in keyword here:
    if answer_state == "Exit" or answer_state is None:
        # Declare the missing_states as the Empty List:
        missing_states = []
        # Using for loop to loop through all_states which is the Original List
        # in order to access the individual items in the all_states:
        for state in all_states:
            # If the state not found in all_states which the User have guessed
            # is not found in the guessed_states:
            if state not in guessed_states:
                # Append the missing_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    answer_state = answer_state.title()
    # If the answer_state is in the all_states:
    if answer_state in all_states:
        # If the User guessed correctly, append it to the List called guessed_states:
        guessed_states.append(answer_state)
        # Instantiating the turtle object:
        t = turtle.Turtle()
        # Showing the turtle cursor:
        t.showturtle()
        # Setting turtle properties for better visibility (adjust as needed):
        # Setting the color of the turtle:
        t.color("red")
        t.pensize(5)
        t.speed("fast")
        # turtle.penup(): This will remove the line from being drawn:
        t.penup()
        # Getting the Horizontal Column of the Data that satisfies the Condition
        # and storing it as the state_data variable:
        state_data = data[data.state == answer_state]
        # Get the state_data.x and state_data.y for the x and y Coordinates.
        # Go to the x and y location for that state itself using the turtle module:
        # Since state_data has the x and y Column itself, you can access it using the state_data.x
        # and the state_data.y just like data.state which is equivalent to data["state"]:
        # It is basically utilizing the x and y Columns itself.
        t.goto(int(state_data.x), int(state_data.y))
        # Write the data into the image itself using the write method:
        t.write(answer_state)

turtle.done()





