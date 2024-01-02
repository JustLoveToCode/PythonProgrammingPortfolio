# Generate some number for us
from random import randint
import turtle


class Point:
    # Creating the variables or properties
    # which is self.x=x and self.y=y

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # point1.x and point1.y, point2.x and point2.y

    def fall_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


# Creating the class of the Rectangle
class Rectangle:
    def __init__(self, point1, point2):
        # These are the Instance Variable of the rectangle
        # point1 and point2 will take in the Point(x1,y1) and Point(x2,y2) respectively
        # which is also derived from the class Point in the first line of code.
        # rectangle.point1.x and rectangle.point1.y, rectangle.point2.x and rectangle.point2.y
        self.point1 = point1
        self.point2 = point2

    # rectangle.area() will invoke this area method.
    # why is it that it is self.point1.x and self.point1.y
    # The reason is because point1 is actually point1.x and probably point1.y
    # point2.x and point2.y
    def area(self):
        return (self.point2.x - self.point1.x) * \
            (self.point2.y - self.point1.y)


# GuiRectangle will inherit from the Rectangle which is also
# the parent itself, hence it will have all the properties and method of the parent rectangle
# GuiRectangle is the child, and Rectangle is the parent
class GuiRectangle(Rectangle):
    # grayed-out parameter mean it is not used yet.
    def draw(self, canvas):
        # Do not draw on the canva
        canvas.penup()
        # Go to that particular coordinate:
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x-self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y-self.point1.y)




class GuiPoint(Point):
    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

# Create the rectangle object
# Using the rectangle class to create the Rectangle Object and having the
# Point class inside that Rectangle that is being created.
# Point(x1,y1) and Point(x2,y2), point1.x, point1.y; point2.x and point2.y
rectangle = GuiRectangle(Point(randint(0, 500), randint(0, 500)),
                      Point(randint(10, 500), randint(10, 500)))

# Print the Rectangle Coordinate:
print("Rectangle Coordinate:",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get the points and the area from the user:
# This will be used to create the instance of the Point class
user_point = GuiPoint(float(input('Guess x:')), float(input('Guess y:')))
# This has no instance, it is just an integer that is used.
# input will create the string type, float() will convert it into integer or number
user_area = float(input("Guess rectangle area:"))

# Print out the game result
# user_point is basically the class Point defined above.
# the class Point has the method of fall_in_rectangle()
print('Your point was inside rectangle', user_point.fall_in_rectangle(rectangle))
# rectangle class has the method area that is defined:
print('Your area is off by:', rectangle.area()-user_area)


myturtle=turtle.Turtle()
# This is the function to invoke to draw the rectangle
rectangle.draw(canvas=myturtle)
# This is the function to invoke to put that particular point that the user have
# input into the terminal
user_point.draw(canvas=myturtle)
# turtle.done() mean you are done drawing using the turtle.
turtle.done()