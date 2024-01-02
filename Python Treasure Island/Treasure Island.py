print("Welcome to the Treasure Island")
optionA = input("Would you like to choose Left or Right\n").lower()
print(optionA)

if optionA == 'left':
    optionB = input("Would you like to Swim or Wait\n").lower()
    print(optionB)
    if optionB == 'wait':
        optionC = input("Which door would you want to go? Red, Yellow or Blue?\n").lower()
        print(optionC)
        if optionC == "yellow":
            print('You win')
        elif optionC == "blue":
            print("You got Freeze! Game Over")
        else:
            print("You are in the Ring of Fire, Game Over")
    else:
        print('You drown while trying to swim across.Game Over')
else:
    print("Game Over")
