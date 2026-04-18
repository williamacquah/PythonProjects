import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def draw_card():
    return random.choice(cards)
def calculate_total(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces > 0:
        total -= 10   # turning one ace from 11 into 1
        aces -= 1
    return total
user_cards = [draw_card(), draw_card()]
computer_cards = [draw_card(), draw_card()]
while True:
    user_total = calculate_total(user_cards)
    computer_total = calculate_total(computer_cards)
    print(f"Your cards: {user_cards}, total = {user_total}")
    print(f"Computer's cards: {computer_cards}, total = {computer_total}")
    if user_total == 21:
        print("You win!")
        break
    elif computer_total == 21:
        print("You lose!")
        break
    if user_total > 21:
        print("You lose!")
        break
    user_choice = input("Do you want to get another card type 'y' for yes and 'n' for no.").lower()
    if user_choice == 'y':
        user_cards.append(draw_card())
        continue
    elif user_choice == 'n':
        break
    else:
        print("Invalid input. Please type 'y' for yes and 'n' for no.")
#Computer turn only if user has not busted and did not already win/lose
user_total = calculate_total(user_cards)
if user_total <= 21 and user_total != 21:
    while calculate_total(computer_cards) < 17:
        computer_cards.append(draw_card())
    computer_total = calculate_total(computer_cards)
    print(f"Your cards: {user_cards}, total = {user_total}")
    print(f"Computer's cards: {computer_cards}, total = {computer_total}")
    if computer_total > 21:
        print("You win!")
    elif computer_total > user_total:
        print("You lose!")
    elif computer_total < user_total:
        print("You win!")
    else:
        print("It's a draw.")