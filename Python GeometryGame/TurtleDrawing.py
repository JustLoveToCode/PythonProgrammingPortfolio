import turtle

# Creating the Object or Canvas Instance
myturtle=turtle.Turtle()

# Do not draw a line for this move
myturtle.penup()

# Going to a Particular/Certain Coordinate
myturtle.goto(50, 75)

# draw the lines again
myturtle.pendown()
# This will move the turtle forward 100px
myturtle.forward(100)
# This will turn the cursor of the turtle to the left
myturtle.left(90)
# This will move the turtle forward 200px
myturtle.forward(200)
# This will turn the cursor of the turtle to the left
myturtle.left(90)
# This will move the turtle forward 100px
myturtle.forward(100)
# This will turn the turtle cursor to the left 90 degree
myturtle.left(90)
# This will move the turtle forward 100px
myturtle.forward(200)

turtle.done()
