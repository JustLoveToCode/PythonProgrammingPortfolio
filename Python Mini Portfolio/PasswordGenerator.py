import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to th PyPassword Generator")

nr_letters = int(input("How many letters would you like to have in your password?\n"))
nr_symbols = int(input("How many symbols would you like to have in your password?\n"))
nr_numbers = int(input("How many numbers would you like to have in your password?\n"))

## Code Syntax
# Initally, it will be empty string:
# password = ""
#
# # Using the for and in keyword:
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     # String Concatenation:
#     password += random_char
#
# for char in range(1, nr_symbols + 1):
#     # String Concatenation
#     password += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     # String Concatenation
#     password += random.choice(numbers)
#
# print(password)

# Declare it as the Empty Array:
password_list = []

# Using the for and in keyword:
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)
    # String Concatenation:
    password_list += random_char

for char in range(1, nr_symbols + 1):
    # String Concatenation
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    # String Concatenation
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)


# Declare it as the Empty String:
password = ""
for char in password_list:
    password += char

print(f"Your Password is {password}")


