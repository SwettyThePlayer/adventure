import random

hp = 10
money = 0
inventory = []

print("You wake up in a dark abandoned cabin...")
print("Find 15 bucks to escape.")

door = input("Which door? (left/middle/right) ").lower().strip()

while hp > 0 and money < 15:
    print()
    print(f"Health: {hp} | Money: {money} | Bag: {inventory}")
    action = input("explore / rest / shop / quit : ").lower().strip()

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
            decision = input("Do you want to drink the brew? (yes/no) ")
            if decision == "yes":
                inventory.remove("brew")
                hp = hp + 5
                print("You drink the brew. +5 hp.")
            elif decision == "no":
                print("You didn't drink it this time.")
            else:
                print("You can't do that here.")
        else:
            print("You rest. +1 health.")
            hp = hp + 1
    elif action == "shop":
        shopitem = random.choice(["axe", "brew"])
        price = random.randint(1, 5)
        print("Hello, Player!")
        print(f"The shop today has: {shopitem} for {price} bucks.")
        buy = input("Do you buy it? (yes/no) ")
        if buy == "yes":
            print(f"You bought the brew. -{price} bucks.")
            money = money - price
            inventory.append(shopitem)
        elif buy == "no":
            print("You didn't take it.")
        else:
            print("You can't do that here.")
    elif action == "quit":
        print("You give up and sit in the cold, dark corner...")
        break
    else:
        print("You can't do that here.")

if money >= 15:
    print("You have enough money to escape. YOU WIN!")
elif hp <= 0:
    print("You lost all your health. GAME OVER!")