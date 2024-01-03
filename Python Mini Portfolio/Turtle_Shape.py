from turtle import Turtle, Screen
import random

colours = ['blue', 'green', 'red', 'cyan', 'black', 'gray']

# Instantiating the Object
turtle = Turtle()

# Draw the turtle shape:
turtle.shape("turtle")
# Draw the color of the turtle:
turtle.color("green")
# Draw outline color of the turtle:
turtle.pencolor('cyan')


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


for shape_side in range(3, 11):
    turtle.color(random.choice(colours))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
