import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
thought = random.randint(1, 100)
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5

while lives > 0:
    guess = int(input("Make a guess:\n "))
    if guess < thought:
        lives -= 1
        if lives > 0:
            print(f"Too low.\n Guess again.\n You have {lives} attempts remaining to guess the number.")
            continue
    elif guess > thought:
        lives -= 1
        if lives > 0:
            print(f"Too high.\n Guess again.\n You have {lives} attempts remaining to guess the number.")
            continue
    elif guess == thought:
        print(f"Correct! You win!.")
        break
    if lives == 0 and guess != thought:
        print(f"You lose. No lives left. The number was {thought}.")
        break