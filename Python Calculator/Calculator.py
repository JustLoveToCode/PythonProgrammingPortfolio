from art import logo

print(f"Welcome to the {logo}")


# Addition:
def add(n1, n2):
    return n1 + n2


# Subtraction:
def subtract(n1, n2):
    return n1 - n2


# Multiplication:
def multiply(n1, n2):
    return n1 * n2


# Division:
def division(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    num1 = float(input("What is the First Number: "))
    num2 = float(input("What is the Second Number: "))

    answer = 0
    for key in operations:
        print(key)

    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation from the line above: ')

        if operation_symbol in operations:
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            user_input = input(
                "Do you want to perform another calculation? Type 'yes' to continue or 'no' to exit: ").lower()
            if user_input == 'yes':
                operation_symbol = input("Pick another operation: ")
                num3 = float(input("What is the next number: "))
                calculation_function = operations[operation_symbol]
                answer = calculation_function(answer, num3)
                print(f"{answer} {operation_symbol} {num3} = {answer}")
            else:
                should_continue = False
        else:
            print("Invalid operation symbol. Please choose a valid operation.")


calculator()
print("Hope you enjoyed using the Calculator")

"Alternative Way of Writing the Code"

"""calculation_function = operations[operation_symbol]"""
"""answer = calculation_function(num1,num2)"""
"""print(answer)"""
