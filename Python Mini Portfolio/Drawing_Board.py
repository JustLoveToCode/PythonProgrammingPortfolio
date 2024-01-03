from turtle import Turtle, Screen

# Instantiating the Turtle Object:
turtle = Turtle()
# Instantiating the Screen Object:
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def clear():
    turtle.clear()
    turtle.home()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
