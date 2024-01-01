def get_average():
    with open("./file/data.txt", 'r') as file:
        # Getting the data from data.txt from the 2nd line onward:
        # Since index start from 0: and store in the data variable:
        data = file.readlines()[1:]
    values = data[1:]
    # Converting from string to integer using the List Comprehension
    # float is used here because temperature is a Continuous Variable and can have Decimal number
    # Using the List Comprehension Method in Python Programming:
    # Using the for loop to iterate through the Python List and then convert it into the float
    values = [float(i) for i in values]
    # Using the sum function and taking the average using the len function
    average_local = sum(values) / len(values)
    # Specify the values that the function should be returning:
    return average_local


# Invoking the function:
average = get_average()
print(average)

# Note:
# If you do not need the calculated average later for your outside function,
# and you are not interested in storing or using the result later.
# In this case, it is preferable to use the return keyword since the
# average = get_average() need to get the value here.
