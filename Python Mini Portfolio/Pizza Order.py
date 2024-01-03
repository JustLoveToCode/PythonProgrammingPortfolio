print("Welcome to the Pizza Order Application")
size = input("What size of the Pizza do you want: S, M or L\n")
add_pepperoni = input("Do you want extra pepperoni: Y or N?\n")
extra_cheese = input("Do you want extra cheese: Y or N?\n")

price = 0
if size == "S":
    price = 15
    print(f"The Small Pizza is ${price}")


elif size == "M":
    price = 20
    print(f"The Medium Pizza is ${price}")

else:
    price = 25
    print(f"The Large Pizza is ${price}")


if add_pepperoni == "Y" and size == 'S':
    price += 3
    print(f"Your bill is ${price}")
elif add_pepperoni == "Y" and size == "M":
    price += 5
    print(f"Your bill is ${price}")
elif add_pepperoni == "Y" and size == "L":
    price += 5
    print(f"Your bill is ${price}")
else:
    print(f"Your bill is ${price} Without the Pepperoni")

if extra_cheese == "Y":
    price += 1
    print(f"Your final bill is ${price}")
else:
    print(f"Your final bill is ${price}")


