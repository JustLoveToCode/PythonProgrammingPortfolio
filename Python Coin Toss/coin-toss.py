while True:
    # read the data into the file with sides.txt
    with open("sides.txt", 'r') as file:
        sides = file.readlines()
    # Getting the user input here:
    side = input("Throw the coin and enter head or tail here: ?") + "\n"
    # Whatever the user have input, append to the sides:
    sides.append(side)
    # write the data into the file with sides.txt:
    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    # Taking the Count of the head and tail using the count method:
    head = sides.count("head\n")
    tail = sides.count("tail\n")

    # Taking the Percentage:
    percentage = head / len(sides) * 100
    percentage_1 = tail / len(sides) * 100

    # Print out the output for the Percentage:
    print(f"Heads: {percentage}%")
    print(f"Tails: {percentage_1}%")
