import colorgram

rgb_colors = []
# This will extract 30 colors from the image.jpg
colors = colorgram.extract('image.jpg', 30)
# This will print out all the Different Colors from the List:
print(colors)


# Using the for keyword for the Different Loop or Iteration:
for color in colors:
    # This will access the properties of the rgb itself:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
# This will append the new_color to the Empty List:
    rgb_colors.append(new_color)
# Once the Iteration has completed, print out the Entire List or Array of Colors:
print(rgb_colors)



