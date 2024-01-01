import random
from art import logo

print(logo)


# Defining the function to pick random cards from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def play_game():
    # Start out with the Blank User Card and the Computer User Card:
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Using the for keyword to loop through the cards List twice using range(2) method:
    # This is to draw 2 cards for both the user_cards and the computer_cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It is a Draw"
        elif computer_score == 0:
            return 'User Lose, Computer has Blackjack'
        elif user_score == 0:
            return 'User win with a Blackjack'
        elif user_score > 21:
            return "User went over, user have lost"
        elif computer_score > 21:
            return "Opponent have Lost, you have won"
        elif computer_score > user_score:
            return "Computer have Won"
        elif computer_score < user_score:
            return "User have Won"

    def calculate_score(cards):
        # Take the 2 Cards and return the Score Calculated:
        if 11 in cards and 10 in cards and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            print("Convert 11 to 1 for Ace")
            cards.remove(11)
            cards.append(1)

        # This return keyword is applicable to both the if statement
        return sum(cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # Checking the Cards of the User and the Computer for the return sum(cards):

        print(f"User first 2 Cards: {user_cards}")
        print(f"Computer first Card: {computer_cards[0]}")

        # Blackjack Criteria:
        if user_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to draw another card, type 'n' to pass\n")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
                if user_score > 21:
                    is_game_over = True
            else:
                is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    final_result = compare(user_score, computer_score)
    print(f"Your final hands: {user_cards}, Your final score: {user_score}")
    print(f"Computer final hands: {computer_cards}, Computer final score: {computer_score}")
    print(final_result)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower() == "y":
    play_game()
