from turtle import Turtle, Screen
import random


direction = [0, 90, 180, 270]
# Instantiating the Turtle Class:
turtle = Turtle()
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex_color

# Properties of the turtle:
turtle.shape('turtle')
turtle.speed('fastest')



def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(1)


screen = Screen()
screen.exitonclick()



