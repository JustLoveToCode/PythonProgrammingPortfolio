from turtle import Turtle, Screen
import random

# Instantiating the screen object:
screen = Screen()
# Setting up the width and height of the screen after creating the object:
screen.setup(width=500, height=400)
# Setting the textinput which is the title and the prompt:
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race,"
                                                          "red, green, orange, blue, black or purple turtle?")

# Creating the List to loop through for different color of the turtle:
colors = ['red', 'green', 'orange', 'blue', 'black', 'purple']
# Creatiing the List to loop through for different coordinate of the turtle:
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

# Set as the Global Variable Assignment:
is_race_on = False
# Creating the different turtle:
for turtle_index in range(0, 6):
    # Instantiating the turtle:
    new_turtle = Turtle(shape='turtle')
    # This will create the penup() method:
    new_turtle.penup()
    # timmy.color(colors[turtle_index): for method to loop through the List:
    new_turtle.color(colors[turtle_index])
    # timmy.goto(): for method to loop through the List:
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # Use the append method to append to the List on the Global Scope:
    all_turtles.append(new_turtle)


# If it is True:
if user_bet:
    is_race_on = True

# This is accessing the Global Variable of is_race_on which
# is changed from False to True:
while is_race_on:
    # Using the for keyword to loop
    for turtle in all_turtles:
        # Checking for the turtle.xcor() which is the x coordinate:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You have won, you choose {user_bet} and the '
                      f' {winning_color} is the winning turtle color.')
            else:
                print(f'You have lost, you choose {user_bet} and the'
                      f' {winning_color} is the winning turtle color.')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
