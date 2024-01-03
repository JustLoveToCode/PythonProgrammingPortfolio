numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# List Comprehension Without any Condition:
squared_numbers = [num ** 2 for num in numbers]
# List Comprehension using the if Condition:
even_numbers = [num for num in numbers if num % 2 == 0]

# Comparing the data between the 2 files that is actually Common:
with open('file1.txt') as file:
    file_1_data = file.readlines()

with open('file2.txt') as file:
    file_2_data = file.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

# Dictionary Comprehension:
# new_dict ={key:value for (key,value) in dictionary.items() if test}
# Taking the existing dictionary and split it into the key and the value.
# The dictionary.items() will basically give you the individual key and value.
# If you need to make some output or calculation, you can do it on the new_value.
# The if test is giving the condition that if it is satisfying a certain condition,
# then you take the value

import random

# This is the List:
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Iterating through the List using the for keyword and create the Dictionary
student_score = {
    student: random.randint(1, 100) for student in names
}

# Iterating through the Dictionary using the for keyword and using the if condition:
passed_student_score = {student_key: score for (student_key, score) in student_score.items()
                        if score > 60}

sentence = "What is the AirSpeed Velocity of an Unladen Swallow"

result = {word: len(word) for word in sentence.split()}

# Code Explanation:
# Using the split to get the Individual word into the List as a String.
# Using the len(word) to give you the length of the word.

# Iterating through the Dictionary which is the (key:value):
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15,
             "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9 / 5 + 32) for (day, temp_c) in weather_c.items()}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key, value) in student_dict.items():
    print(key)
    print(value)

# Converting the Dictionary into the DataFrame in the form of Table:
# Putting the data into the DataFrame:
import pandas

# Put it in the form of table using the DataFrame keyword:
data = pandas.DataFrame(student_dict)

# Another Way of Using Dataframes when it is String inside the List:
list = ["Geeks", "For", "Geeks", "is", "portal", "for", "Geeks"]

# Create the table with the data:
df = pandas.DataFrame(list)

# Using for keyword to loop through the data.items() to get
# the key and value pairing:
for (key, value) in data.items():
    print(key)
    print(value)

# Using the iterrows() itself to print out each Individual Row:
for (index, row) in data.iterrows():
    print(index)
    print(row)
    # This will print out the item value itself:
    print(row.student)
