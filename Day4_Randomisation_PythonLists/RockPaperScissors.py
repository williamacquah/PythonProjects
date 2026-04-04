import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer = random.randint(0,2)
if choice < 0 or choice > 2:
    print("Invalid choice. You Lose")
elif choice == computer:
    print("It was a draw. Try again.")
elif choice == 0 and computer == 1:
    print(rock)
    print("Computer chose:\n", paper)
    print("You lose")
elif choice == 0 and computer == 2:
    print(rock)
    print("Computer chose:\n", scissors)
    print("You win")
elif choice == 1 and computer == 0:
    print(paper)
    print("Computer chose:\n", rock)
    print("You win")
elif choice == 1 and computer == 2:
    print(paper)
    print("Computer chose:\n", scissors)
    print("You lose")
elif choice == 2 and computer == 0:
    print(scissors)
    print("Computer chose:\n", rock)
    print("You lose")
elif choice == 2 and computer == 1:
    print(scissors)
    print("Computer chose:\n", paper)
    print("You win")