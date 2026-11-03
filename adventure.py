hp = 10
money = 0

print("You wake up in a dark abandoned cabin...")
print("There are three doors: left, middle and right...")

door = input("Which door? (left/middle/right) ").lower().strip()

if door == "left":
    print("A rat bites you!")
    hp = hp - 2
elif door == "right":
    print("You found some money")
    money = money + 5
else:
    print("You stand still. Nothing happens.")

print(f"Health: {hp} | Money: {money}")