import random

hp = 10
money = 0
inventory = []

print("You wake up in a dark abandoned cabin...")
print("Find 15 bucks to escape.")

door = input("Which door? (left/middle/right) ").lower().strip()

while hp > 0 and gold < 15:
    print()
    print(f"Health: {hp} | Money: {money} | Bag: {inventory}")
    action = input("explore / rest: ").lower().strip()

    if action == "explore":
        event = random.choice(["squirrel", "money", "item", "nothing"])
        if event == "squirrel":
            damage = random.randint(1, 4)
            if "axe" in inventory:
                damage = damage - 1
                print("The axe protects you!")
            hp = hp - damage
            print(f"A crazy squirrel attacks you! You lose {damage} health.")
        elif event == "money":
            found = random.randint(1,3)
            money = money + found
            print(f"You found {found} bucks!")
        elif event == "item":
            item = random.choice(["axe", "brew"])
            inventory.append(item)
            print(f"You find a(n) {item}")
        else:
            print("Just an empty room. Spooky.")
    elif action == "rest":
        if "brew" in inventory:
            inventory.remove("brew")
            hp = hp + 5
            print("You drink the brew. +5 hp.")
        else:
            print("You rest. +1 health.")
            hp = hp + 1
    elif action == "quit":
        print("You give up and sit in the cold, dark corner...")
        break
    else:
        print("You can't do that here.")

if money >= 15:
    print("You have enough money to escape. YOU WIN!")
elif hp <= 0:
    print("You lost all your health. GAME OVER!")