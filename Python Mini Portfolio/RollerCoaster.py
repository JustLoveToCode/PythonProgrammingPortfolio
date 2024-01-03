print("Welcome to the RollerCoaster")

height = float(input("What is your height in cm?"))

# Declared as Global Variable
bill = 0

if height >= 120:
    print("You can ride the rollerCoaster!")

    age = int(input("What is your age\n"))
    # Using the if else statement inside
    if age < 12:
        bill = 5
        print(f"Child Ticket ${bill}")
    elif 12 < age <= 18:
        bill = 7
        print(f"Youth Ticket ${bill} ")
    elif 45 <= age <= 55:
        print('Everything is going to be ok, it is free ride on us')
    else:
        bill = 12
        print(f"Adult Ticket: ${bill} ")

    want_photo = input("Do you want a photo or not? Y or N\n")
    if want_photo == 'Y' and age < 12:
        bill += 3
        print(f"Your ticket will be {bill} ")
    elif want_photo == "Y" and 12 < age < 18:
        bill += 3
        print(f"Your ticket will be {bill}")
    elif want_photo == "Y" and age > 12:
        bill += 3
        print(f"Your ticket will be {bill}")
    else:
        print(f"Your ticket will be {bill} without the ticket ")
else:
    print("Sorry you have to grow taller")
