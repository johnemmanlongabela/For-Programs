import random

number_to_guess = random.randint(1,50)

while True:
    try:
        guess = int(input("Guess a number between 1 and 50: "))
        if guess < number_to_guess:
            print("Too low")
        elif guess > number_to_guess:
            print("Too high")
        else:
            print("You guessed correctly")
            break
    except ValueError:
        print("Please enter a number")