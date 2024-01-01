password = input('Enter your Password')
# Since it is Dictionaries, it will be {} instead of []
# Accessing Dictionary using result["digit"] here:
result = {}

# Using the len method to see the Length of your password:
# This length can be either True or False:
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# digit is initially set to False
digit = False
# Iterating through the string password
for i in password:
    # Checking through each individual characters in the password
    # Check if all the characters in the strings are Digits:
    if i.isdigit():
        digit = True

# Exiting the for loop
# digit is either True or False
result["digit"] = digit
# This digit can be True or False

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase
# This uppercase can be True or False

# The all Condition in the List is Satisfied
# if EVERYTHING in the List is True
# '==' is the Equality Sign on whether it is True or False:
# result.values() here will get you all the values in the Dictionary:
if all(result.values()):
    print('It is a STRONG Password')
else:
    print('It is a WEAK Password')
