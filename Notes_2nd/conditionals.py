#EG 2nd Conditionals Notes

#num = float(input("Enter a number: "))

#if num > 0:
    #print(f"The number {num} is positive.")
#elif num < 0:
    #print(f"The number {num} is negative.")
#else:
    #print(f"The number {num} is zero.")

import random
monster_hp = 30
dmg_modifier = 2
atk_bonus = 3
player_hp = 25

roll = random.randint(1,20)

if roll == 20:
    print(f"you rolled a crit! double your damage.")
    attack = random.randint(1,8) + random.randit(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll+atk_bonus> 10:
    print(f"you hit.")
    attack = random.randint(1,8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster!")
elif roll <=10:
    if roll == 1:
        print(f"You rollled a critical failure! The monster gets a free attack!")
        damage = random.randint(1,10) +2
        player_hp -= damage
        print(f"You took {damage} you now have {player_hp} HP.")
    else:
     print(f"you missed!")
else:
    print(f"That shouldn't be possible.")

print("Your turn is over.")

if monster_hp and monster_hp > 0:
    print("It is the monsters turn")
else:
    print("the monster is dead")