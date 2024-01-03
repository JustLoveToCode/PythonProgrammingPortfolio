print("Welcome to the Love Calculator")
name1 = input("What is your Name \n")

name2 = input("What is their Name\n")

# To work out the Love Score between the 2 Person
# Take Both the person names for the number of times the letters in the words
# "TRUE" occur, then check for the number of times the letters in the word LOVE occurs.
# Then Combine the numbers to take into 2 Digits.


# Concatenating the String together
combined_string = name1 + name2
# Convert all to the Lowercase:
lower_case_string = combined_string.lower()

# Using the count method:
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

# Sum up the number of occurrence for true:
true = t + r + u + e

# Using the count method
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your Love Score is {love_score},"
          f"you go together like coke and mentos ")
elif 40 <= love_score < 50:
    print(f"Your Love Score is {love_score}, you are "
          f"alright together.")
else:
    print(f"Your score is {love_score}")
