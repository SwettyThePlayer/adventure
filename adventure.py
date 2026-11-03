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
        print("You find 2 bucks.")
        money = money + 2
        hp = hp - 1
    elif action == "rest":
        print("You rest. +1 health.")
        hp = hp + 1
    else:
        print("You can't do that here.")

print("The game is over.")