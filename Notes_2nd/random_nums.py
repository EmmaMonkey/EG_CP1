# EG 2nd Random Numbers Notes
import random

# Examples of random numbers
#print(random.random()) # Float between 0 and 1
#print(random.randint(1,6))


name = input("What is your name: \n").strip().title()

# Fifa Stat creator
stat_one = random.randint(1,10) + random.randint(1,99)
stat_two = random.randint(1,10) + random.randint(1,99)
stat_three = random.randint(1,10) + random.randint(1,99)
stat_four = random.randint(1,10) + random.randint(1,99)
stat_five = random.randint(1,10) + random.randint(1,99)
stat_six = random.randint(1,10) + random.randint(1,99)
stat_seven = random.randint(1,10) + random.randint(1,99)

print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

speed = int(input("Which stat are you making your speed")) 
shot = int(input("Which stat are you making your shot")) 
passing = int(input("Which stat are you making your passing")) 
dribbling = int(input("Which stat are you making your dribbling")) 
defending = int(input("Which stat are you making your defending")) 
physical = int(input("Which stat are you making your physical")) 
Overall = int(input("Which stat are you making your Overall")) 