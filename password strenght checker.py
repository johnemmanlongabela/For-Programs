import re

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search('[a-z]', password):
        strength += 1
    if re.search('[A-Z]', password):
        strength += 1
    if re.search('[0-9]', password):
        strength += 1
    if re.search('[.]', password):
        strength += 1

    return strength


def main():
    password = input()
    strength = check_password_strength(password)

    if strength == 5:
        print("Password Strength: Very Strong!")
    if strength == 4:
        print("Password Strength: Strong!")
    if strength == 3:
        print("Password Strength: Moderate!")
    if strength == 2:
        print("Password Strength: Weak!")
    if strength == 1:
        print("Password Strength:Very Weak!")


if __name__ == '__main__':
    main()