import random

hp = 10
money = 0

print("You wake up in a dark abandoned cabin...")
print("Find 15 bucks to escape.")

door = input("Which door? (left/middle/right) ").lower().strip()

while hp > 0 and gold < 15:
    print()
    print(f"Health: {hp} | Money: {money}")
    action = input("explore / rest: ").lower().strip()

    if action == "explore":
        event = random.choice(["squirrel", "money", "nothing"])
        if event == "monster":
            damage = random.randint(1, 4)
            hp = hp - damage
            print(f"A crazy squirrel attacks you! You lose {damage} health.")
        elif event == "money":
            found = random.randint(1,3)
            money = money + found
            print(f"You found {found} bucks!")
        else:
            print("Just an empty room. Spooky.")
    elif action == "rest":
        print("You rest. +1 health.")
        hp = hp + 1
    else:
        print("You can't do that here.")

print("The game is over.")