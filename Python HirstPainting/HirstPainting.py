from turtle import Turtle, Screen
import colorgram
import random

# Declare Empty Array:
rgb_colors = []
colors = colorgram.extract('image.jpg', 100)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    # This will create the tuple that is immutable:
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)


# Instantiating turtle object:
turtle = Turtle()


# The Starting Position of the turtle:
turtle.hideturtle()
turtle.setheading(225)
turtle.penup()
turtle.forward(250)
turtle.setheading(0)
turtle.speed('fastest')

counter = 0

while counter < 9:
        for _ in range(9):
            random_color = random.choice(rgb_colors)
            hex_color = '#%02x%02x%02x' % random_color
            turtle.dot(20, hex_color)
            turtle.penup()
            turtle.forward(50)
            turtle.pendown()

        turtle.penup()
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.penup()
        turtle.forward(450)
        turtle.setheading(0)

        counter += 1


# Instantiating screen object:
screen = Screen()
# When it clicked, it exited
screen.exitonclick()


