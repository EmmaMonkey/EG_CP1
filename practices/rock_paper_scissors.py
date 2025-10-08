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
    user = input("Rock, paper, or scissors? Or type quit to stop playing: ").lower()

    if user == "quit":
        print("Bye Monkey!")
        break
    if user not in choices:
        print("That's not one of the choices. ")
        continue

    Me = random.choice(choices)
    print(f"I chose {Me}.")

    if user == Me:
        print("It's a tie!\n")
    elif (user == "rock" and Me == "scissors") or \
         (user == "scissors" and Me == "paper") or \
         (user == "paper" and Me == "rock"):
        print("You win!\n")
    else:
        print("I beat you!\n")