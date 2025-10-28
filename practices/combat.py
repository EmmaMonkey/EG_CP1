# EG 2nd Combat Program

import random


def player_turn(player, monster):
    print("\nWhat would you like to do?")
    print("1. Normal Attack")
    print("2. Wild Attack (double damage but take some yourself)")
    print("3. Drink a healing potion")
    print("4. Flee")
    choice = input("> ")

    if choice == "1":
        attack = random.randint(1, 20) + 3
        if attack > monster["defense"]:
            damage = random.randint(1, 8) + 4
            monster["health"] -= damage
            print(f"You hit! The {monster['name']} took {damage} damage.")
        else:
            print("Your attack missed!")

    elif choice == "2":
        attack = random.randint(1, 20) + 3
        if attack > monster["defense"]:
            damage = (random.randint(1, 8) + 4) * 2
            monster["health"] -= damage
            self_damage = random.randint(1, 6)
            player["health"] -= self_damage
            print(f"Wild attack! You deal {damage} but take {self_damage} yourself.")
        else:
            print("You swung wildly but missed!")

    elif choice == "3":
        heal = 9
        player["health"] += heal
        print(f"You drink a potion and heal {heal} HP.")

    elif choice == "4":
        if random.choice([True, False]):
            print("You successfully fled from battle!")
            monster["health"] = 0
        else:
            print("You tried to flee but the monster blocks your path!")

    else:
        print("Invalid choice, turn wasted.")

def monster_turn(player, monster):
    print(f"\nThe {monster['name']} attacks!")
    attack = random.randint(1, 20)
    if attack > player["defense"]:
        damage = random.randint(1, 6) + 3
        player["health"] -= damage
        print(f"The {monster['name']} hits you for {damage} damage!")
    else:
        print(f"The {monster['name']} missed its attack!")


def main():
    print("Welcome to training! First I need to know some things about you!")
    name = input("What is your name? ")
    print("\nWhat class of fighter are you?")
    print("1. Fighter\n2. Mage\n3. Rogue")
    class_choice = input("> ")

    if class_choice == "1":
        player = {"name": name, "health": 30, "defense": 14}
    elif class_choice == "2":
        player = {"name": name, "health": 25, "defense": 10}
    else:
        player = {"name": name, "health": 20, "defense": 12}

    monster = {"name": "Dire Wolf", "health": 35, "defense": 13}

    print(f"\nGreat, here are your stats:")
    print(f"Health: {player['health']}")
    print(f"Defense: {player['defense']}")
    print("Attack: D20 + 3")
    print("Damage: D8 + 4")

    print(f"\nYou are being attacked by a {monster['name']}!")
    turn = random.choice(["player", "monster"])
    print(f"{'You' if turn == 'player' else 'The monster'} move first!")

    while player["health"] > 0 and monster["health"] > 0:
        if turn == "player":
            player_turn(player, monster)
            turn = "monster"
        else:
            monster_turn(player, monster)
            turn = "player"

        print(f"\nYour HP: {player['health']}")
        print(f"{monster['name']} HP: {monster['health']}")

        if player["health"] <= 0 or monster["health"] <= 0:
            break

    print("\n--- BATTLE RESULTS ---")
    if player["health"] <= 0:
        print("You have been defeated you loser!")
    elif monster["health"] <= 0:
        print("You defeated the monster Your aura farming for real!")
    else:
        print("The battle ended unexpectedly.")

main()
