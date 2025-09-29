# EG 2nd Fix Game 

import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)  # Picks a random number between 1–100
    max_attempts = 10
    attempts = 0
    game_over = False
    
    while not game_over:
        # BUG 1: input() gives back a STRING, but we need an INTEGER
        # Type: Runtime bug
        # Why: Comparing a string with a number caused a crash when using >, <, or ==
        guess = int(input("Enter your guess: "))
        
        # BUG 2: Attempts were never increased
        # Type: Logic bug
        # Why: Without attempts += 1, the max_attempts check never worked (infinite loop possible)
        attempts += 1
        
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        
        # BUG 3: Needed "elif", not "if"
        # Type: Logic bug
        # Why: If we left it as "if", the program might still check other conditions even after winning
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        
        # BUG 4: The "continue" was unnecessary
        # Type: Logic bug
        # Why: It skipped the natural loop flow and made code harder to run. Removing fixed it.

    print("Game Over. Thanks for playing!")

start_game()