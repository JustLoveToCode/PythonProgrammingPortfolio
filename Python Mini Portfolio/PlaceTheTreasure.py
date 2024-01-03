import random

#        col1    col2    col3
row1 = ["Box 1", "Box 2", "Box 3"]
row2 = ["Box 4", "Box 5", "Box 6"]
row3 = ["Box 7", "Box 8", "Box 9"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? Input Column and Row (e.g., '23' for column 2, row 3)\n")

# Extracting horizontal and vertical values
horizontal = int(position[0])
vertical = int(position[1])

# Adjusting for zero-based index
selected_row = map[vertical - 1]
treasure = selected_row[horizontal - 1]

print(f"The treasure is located in {treasure}!")
