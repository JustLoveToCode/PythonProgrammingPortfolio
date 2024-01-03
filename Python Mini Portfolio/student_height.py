# This will give you the Array or List after the split keyword:
student_heights = input("Input the List of the Student Height with Space in Between Number\n").split()

# Using the range method:
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Initialize it as total_height = 0
total_height = 0

# Iterating through the List:
# Using the for loop:
for height in student_heights:
    # Initial value of total_height is actually 0
    total_height += height

# Iterating through the List:
# Using the for loop:
number_of_students = 0
for student in student_heights:
    number_of_students += 1


# Calculating the Average Height:
average_height = round(total_height / number_of_students)
print(average_height)
