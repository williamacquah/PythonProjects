import random
from art import logo

EASY_LEVEL_LIVES = 10
HARD_LEVEL_LIVES = 5

def check_answer(guess, thought, lives):
    """Checks answer against guess, returns the number of turns remaining"""
    if guess < thought:
        lives -= 1  # decrement first
        print(f"Too low.\nGuess again.\nYou have {lives} attempts remaining.")
        return lives
    elif guess > thought:
        lives -= 1
        print(f"Too high.\n Guess again.\n You have {lives} attempts remaining.")
        return lives
    else:  # guess == thought
        print("Correct! You win!")
        return lives

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == "easy":
        return EASY_LEVEL_LIVES
    elif difficulty == "hard":
        return HARD_LEVEL_LIVES

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    thought = random.randint(1, 100)
    turns = set_difficulty()
    guess = None
    while guess != thought:
        guess = int(input("Make a guess:\n "))
        turns = check_answer(guess, thought, turns)
        if turns == 0:
            print(f"You've run out of guesses. The number was {thought}, you lose.")
            return

game()
