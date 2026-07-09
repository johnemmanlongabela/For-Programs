operator = input("Enter your operator (+-*/): ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if operator == "+":
    result = (num1 + num2)
    print(round(result, 3))
elif operator == "-":
    result = (num1 - num2)
    print(round(result, 3))
elif operator == "*":
    result = (num1 * num2)
    print(round(result, 3))
elif operator == "/":
    result = (num1 / num2)
    print(round(result, 3))
else:
    print("Operator not recognized")