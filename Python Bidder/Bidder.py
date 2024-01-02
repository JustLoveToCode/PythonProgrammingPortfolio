from art import logo

print(logo)

# Declaring the Empty Dictionary:
bid = {}

bidding_finished = False
# While it is True:
while not bidding_finished:
    name = input("What is your Name?\n")
    price = int(input("What is your Bid?\n$"))
    bid[name] = price
    print(bid)
    user_answer = input("Are there any Bidders Left? yes or no?").lower()
    if user_answer == "no":
        bidding_finished = True  # Set the flag to exit the loop
    elif user_answer != "yes":
        print("Invalid input. Please enter 'yes' or 'no'.")
    # Continue the loop if user_answer is "yes" or any other input

# Code continues after the while loop
highest_bid = 0
winner = ""
for bidder in bid:
    bid_amount = bid[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The Winner is {winner} with the bid of ${highest_bid}")






