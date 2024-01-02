import random

from hangman_words import word_list
from hangman_art import stages, logo


print(logo)
random = random.choice(word_list)

word_length = len(random)

lives = 6

display = []

for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    user_input = input("Guess a Letter\n").lower()



    if user_input in display:
        print(f"You have already guess that {user_input}")


    # Using the for loop:
    for position in range(word_length):
        letter = random[position]
        if letter == user_input:
            display[position] = letter
    if user_input not in random:
        lives -= 1
        print(f"You have chosen letter {user_input}, you lose a life,"
              f"your life is currently {lives}")
        print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("You have Lost the Game")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You have Won the Hangman")
