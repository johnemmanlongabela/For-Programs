import string
import random

def generate_password(lenght, include_uppercase, include_lowercase, include_numbers, include_symbols):
    if lenght < (include_uppercase + include_lowercase + include_numbers + include_symbols):
        raise ValueError('Password is too short!')

    password = ''

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_lowercase:
        password += random.choice(string.ascii_lowercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_symbols:
        password += random.choice(string.punctuation)

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    for _ in range (lenght - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    lenght = int(input('Enter password length: '))
    include_uppercase = input('Include uppercase? (y/n): ').lower() == 'y'
    include_lowercase = input('Include lowercase? (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers? (y/n): ').lower() == 'y'
    include_symbols = input('Include symbols? (y/n): ').lower() == 'y'
    try:
        password = generate_password
        print(password)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
     main()