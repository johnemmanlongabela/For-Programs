import random

colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']

balance = 100

print("=" * 40)
print("🎰 COLOR SLOT MACHINE 🎰")
print("=" * 40)
print("Starting Balance: $100")

while balance > 0:
    print(f"\nCurrent Balance: ${balance}")


    try:
        bet = int(input("Enter your bet (0 to quit): $"))

        if bet == 0:
            print("Thanks for playing!")
            break

        if bet < 0:
            print("Bet must be positive.")
            continue

        if bet > balance:
            print("You don't have enough money!")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue


    slot1 = random.choice(colors)
    slot2 = random.choice(colors)
    slot3 = random.choice(colors)

    print("\nSpinning...\n")

    print(f"| {slot1:^8} | {slot2:^8} | {slot3:^8} |")


    if slot1 == slot2 == slot3:
        winnings = bet * 10
        balance += winnings
        print(f"\n🎉 JACKPOT! You won ${winnings}!")

    elif slot1 == slot2 or slot2 == slot3 or slot1 == slot3:
        winnings = bet * 2
        balance += winnings
        print(f"\n😊 Two colors matched! You won ${winnings}!")

    else:
        balance -= bet
        print(f"\n😢 No match. You lost ${bet}.")

    if balance <= 0:
        print("\nGame Over! You're out of money.")

print(f"\nFinal Balance: ${balance}")