import random
from art import logo

print(logo)

print('Welcome to the Number Guessing Game')
print('I am thinking of a number between 1 and 100')

while True:
    Difficulty = input('Choose the Difficulty, Type easy or hard\n').lower()
    if Difficulty in ['easy', 'hard']:
        break
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")

guess = random.choice(range(1, 101))
end_game = False


def difficulty_level():
    if Difficulty == 'easy':
        return 10
    elif Difficulty == 'hard':
        return 5


attempt = difficulty_level()


def attempt_game():
    global attempt, end_game
    while not end_game:
        user_guess = int(input("Make a Guess by Choosing a Number\n"))

        if Difficulty == "easy":
            if guess > user_guess:
                print("Number is too Low, Guess Higher")
                attempt -= 1
                print(f"You have {attempt} attempts left")
                if attempt == 0:
                    print('This is Game Over')
                    end_game = True
            elif guess < user_guess:
                print("Number is too High, Guess Lower")
                attempt -= 1
            elif guess == user_guess:
                print("You have made the correct guess")
                end_game = True
        elif Difficulty == "hard":
            if guess > user_guess:
                print("Number is too Low, Guess Higher")
                attempt -= 1
                print(f"You have {attempt} attempts left")
                if attempt == 0:
                    print('This is Game Over')
                    end_game = True
            elif guess < user_guess:
                print("Number is too High, Guess Lower")
                attempt -= 1
            elif guess == user_guess:
                print("You have made the correct guess")
                end_game = True


attempt_game()
