import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

while True:
    User_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissor\n"))
    print("User Choose")
    print(game_images[User_choice])
    Computer_choice = random.randint(0, 2)
    print("Computer Choose")
    print(game_images[Computer_choice])


    if Computer_choice == User_choice:
        print("It is a draw, let play again")
        continue
    elif Computer_choice == 0 and User_choice == 1:
        print("User Win!")
    elif Computer_choice == 0 and User_choice == 2:
        print("Computer Win!")
    elif Computer_choice == 1 and User_choice == 0:
        print("Computer Win!")
    elif Computer_choice == 1 and User_choice == 2:
        print("User Win!")
    elif Computer_choice == 2 and User_choice == 0:
        print("User Win!")
    elif Computer_choice == 2 and User_choice == 1:
        print("User Win!")
    elif User_choice >= 3 or User_choice < 0:
        print("You type in an Invalid Choice")
        continue

    play_again = input("Do you want to play again? type yes or no")
    if play_again.lower() != "yes":
        break








