import random

from art import logo, vs
from game_data import data

def get_two_indices():
    index1 = random.randint(0, len(data) - 1)
    index2 = random.randint(0, len(data) - 1)
    while index1 == index2:
        index2 = random.randint(0, len(data)-1)
    return index1, index2

def check_choice(choice, index1, index2):
    if choice == 'a' and data[index1]['follower_count'] > data[index2]['follower_count']:
        return True
    elif choice == 'b' and data[index1]['follower_count'] < data[index2]['follower_count']:
        return True
    else:
        return False


def game():
    print(logo)
    score = 0
    while True:
        index1, index2 = get_two_indices()
        print(f"Campare A: {data[index1]['name']}, {data[index1]['description']}, from {data[index1]['country']}.")
        print(vs)
        print(f"against B: {data[index2]['name']}, {data[index2]['description']}, from {data[index2]['country']}.")
        choice = input("Who has more instagram followers? Type 'A' or 'B': ").lower()
        if check_choice(choice, index1, index2):
            score += 1
            print(f"You're correct! Your score is {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            break


game()