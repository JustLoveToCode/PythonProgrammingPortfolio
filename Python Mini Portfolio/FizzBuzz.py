number = 0
for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        print('Fizz')
    elif number % 5 == 0 and number % 3 != 0:
        print('Buzz')
    elif number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    else:
        print(number)

# Code
# If the number is divisible by 3 and not divisible by 5:
# print Fizz
# If the number is divisible by 5 and not divisible by 3:
# print Buzz
# If the number is divisible by 3 and divisible by 5:
# print FizzBuzz

