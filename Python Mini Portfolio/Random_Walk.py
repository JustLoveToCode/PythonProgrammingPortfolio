from turtle import Turtle, Screen
import random

direction = [0, 90, 180, 270]
# Instantiating the Turtle Object:
turtle = Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color


# Creating the Shape of the turtle:
turtle.shape('turtle')

# Draw the Color of the turtle:
turtle.color('red')

turtle.pencolor('cyan')
# Changing the Size of the Brush:
turtle.pensize(20)

# Changing the Speed of the Turtle:
turtle.speed('fastest')

for _ in range(200):
    turtle.color(random_color())
    # Turtle to move forward, this will move the turtle
    # forward in a specific direction:
    turtle.forward(30)
    # It is the method that will change the Orientation
    # of the turtle at the given angle:
    turtle.setheading(random.choice(direction))

# Instantiating the Screen class:
screen = Screen()
# Exit on Click:
screen.exitonclick()
