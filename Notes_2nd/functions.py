# EG 2nd Functions Notes
# All imports 
# Set Global Variables
num = 0
player_hp = 100
monster_hp = 100

# Write your functions
def add(x,y):
    return x+y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial 

def attack(dmg, turn):
    global player_hp
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg


# Write the rest of your code
while num < add(5,5):
    print("Duck")
    num +=1 
print("Goose")
print(f"Result is: {add(-654386878523,5237983)}")
total = add(3874983274,34)
print(add(add(3.14,.85), 10))
add(42,7)

print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Xavier's initials are: {initials("Xavier LaRose")}")
monster_hp, player_hp = attack(15, "monster")
print(f" Player Health: {player_hp}")
print(f" Monster Health: {monster_hp}")

monster_hp, player_hp = attack(15, "player")
print(f" Player Health: {player_hp}")
print(f" Monster Health: {monster_hp}")

print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")