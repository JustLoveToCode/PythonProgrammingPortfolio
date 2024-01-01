from converter import convert
from refactor import parse

feet_inches = input('Enter the feet and inches with Space in between:')

parsed = parse(feet_inches)

print(parsed)
# {'feet' : 3.0, 'inches': 12.0}--This is of the Type Dictionary

# Accessing the Dictionary Value using the Key:
# Passing it back to the function for convert(a,b):
# Convert the result using the convert function:
# Accessing the values using the Dictionary Method of Key Value Pairing:
result = convert(parsed['feet'], parsed['inches'])

print(result)
# 1.2192

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

# If-else Conditional Operator:
if result < 1:
    print('You are eligible for the slide')
else:
    print('You are not eligible for the slide')
