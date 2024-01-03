import math

test_h = int(input("What is the Height of the Wall?\n"))
test_w = int(input("What is the Width of the Wall?\n"))

coverage = 5
amount_of_paint = 0


def paint_calc(height, width, cover):
    amount_of_paint = math.ceil(height * width / coverage)
    print(f"{amount_of_paint} is needed to paint the wall")


paint_calc(height=test_h, width=test_w, cover=coverage)
