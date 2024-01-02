import random
from game_data import data

game_over = False

while not game_over:
    random_choices_A = random.sample(data, 1)
    random_choices_B = random.sample(data, 1)

    while random_choices_A == random_choices_B:
        random_choices_A = random.sample(data, 1)
        random_choices_B = random.sample(data, 1)

    print(f"Compare A, {random_choices_A[0]['name']}, a {random_choices_A[0]['description']} from "
          f"{random_choices_A[0]['country']}")
    print(f"Against B, {random_choices_B[0]['name']}, a {random_choices_B[0]['description']} from "
          f"{random_choices_B[0]['country']}")

    user_choice = input("Who has more followers? A or B: ").upper()

    if random_choices_A[0]['follower_count'] > random_choices_B[0]['follower_count'] and user_choice == 'A':
        print('You choose A, you are Correct')

        while True:
            user_choice_general = input('Do you want to play again? Y or N?').upper()
            if user_choice_general == "Y":
                break
            else:
                game_over = True
                break

            # B is Randomized again:
            random_choices_B = random.sample(data, 1)
            # If Randomized B has a higher follower counts than A:
            if random_choices_B[0]['follower_count'] > random_choices_A[0]['follower_count']:
                print(f"Now compare B, {random_choices_B[0]['name']} with A, {random_choices_A[0]['name']}:")

                user_choice_C = input("Who has more followers? B or A: ")

                if user_choice_C == 'B':
                    print('You are Correct')
                    random_choices_A = random.sample(data,1)
                else:
                    print('You choose A, you are Wrong')
                    game_over = True
                    break

                # If A has a higher follower count than B:
            elif random_choices_B[0]['follower_count'] < random_choices_A[0]['follower_count']:
                    print(f"Now compare B, {random_choices_B[0]['name']} with A, {random_choices_A[0]['name']}:")
                    user_choice_C = input("Who has more followers? A or B: ")

                    if user_choice_C == 'A':
                        print('You choose A, you are Correct')
                        random_choices_B = random.sample(data, 1)
                    else:
                        print('You choose A, you are Wrong')
                        game_over = True
                        break

    elif random_choices_A[0]['follower_count'] > random_choices_B[0]['follower_count'] and user_choice == 'B':
        print('You choose B, you are Wrong')
        game_over = True

    elif random_choices_B[0]['follower_count'] > random_choices_A[0]['follower_count'] and user_choice == 'A':
        print('You choose A, you are Wrong')
        game_over = True

    elif random_choices_B[0]['follower_count'] > random_choices_A[0]['follower_count'] and user_choice == 'B':
        print('You choose B, you are Correct')
        # While the above elif statement is True:
        while True:
            user_choice_general = input('Do you want to play the game again? Y or N?').upper()
            if user_choice_general == 'Y':
                break
            else:
                is_game_over = True
                break

            # A is randomized again
            random_choices_A = random.sample(data, 1)
            # If randomized A has a Higher Follower Count than B:
            if random_choices_B[0]['follower_count'] > random_choices_A[0]['follower_count']:
                print(f"Now Compare B, {random_choices_B[0]['name']} with A, {random_choices_A[0]['name']}:")
                user_choice_C = input("Who have more followers? A or B: ")

                if user_choice_C == "B":
                    print('You are right')
                    random_choices_A = random.sample(data, 1)
                else:
                    print('You are wrong')
                    game_over = True
                    break
            elif random_choices_A[0]['follower_count'] > random_choices_B[0]['follower_count']:
                print(f"Now Compare B, {random_choices_B[0]['name']} with A, {random_choices_A[0]['name']}:")
                user_choice_C = input("Who have more followers? A or B:")

                if user_choice_C == 'A':
                    print('You are right')
                    random.choices_A = random.sample(data, 1)
                else:
                    print('You are wrong')
                    game_over = True
                    break


    else:
        print('Invalid choice. Please select either "A" or "B".')


