# The Try and Except in Python Programming:
try:
    user_input = int(input('Enter total value:'))
    user_second_input = int((input('Enter Value:')))
    percentage = user_second_input / user_input * 100
    print(percentage)
except ValueError:
    print('You need to enter a number, Run the program again.')
except ZeroDivisionError:
    print('Your total value cannot be zero.')


