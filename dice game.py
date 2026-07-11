import random

while True:
    choice = input(" Game Start! Roll Dice!(y/n):").lower()
    if choice == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)
        print(f'({die1}, {die2}, {die3})')
    elif choice == "n":
        print("Game Over!")
        break
    else:
        print("Invalid Input!")
