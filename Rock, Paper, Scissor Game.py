import random

emojis = {'R':'🗿', 'P':'📃', 'S':'✂'}
choices = ('R', 'P', 'S')

while True:
    user_choice = input('Rock, Paper, Scissor, (R, P, S): ').upper()
    if user_choice not in choices:
        print('Invalid Input')

    computer_choice = random.choice(choices)

    print(f'User Chose {emojis[user_choice]}')
    print(f'Computer Chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Draw!')
    elif user_choice == 'R' and computer_choice == 'S':
        print('You Win!')
    elif user_choice == 'S' and computer_choice == 'P':
        print('You Win!')
    elif user_choice == 'P' and computer_choice == 'R':
        print('You Win!')
    else:
        print('You Lose!')

    should_continue = input('Continue?(y/n): ').lower()
    if user_choice == 'n':
        print('Restart Game')
    break