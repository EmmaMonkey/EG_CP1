# EG 2nd  Rock Paper Scissors
import random
import time

# Rock
print("Welcome to Rock, Paper, Scissors! ")
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Rock, paper, or scissors? (or type 'quit' to stop): ").lower()

    if user == "quit":
        print("Bye! Thanks for playing.")
        break
    if user not in choices:
        print("That's not a valid choice. Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose {computer}.")

    if user == computer:
        print("It's a tie!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!\n")
    else:
        print("Computer wins!\n")