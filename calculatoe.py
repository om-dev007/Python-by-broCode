# Python Calculator

operator = input("Enter an operator (+ - * /): ")
if operator == "":
    print('Invalid operator')
elif operator == "+":
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    print(num1 + num2)
elif operator == "-":
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    print(num1 - num2)
elif operator == "*":
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    print(num1 * num2)
elif operator == "/":
    num1 = float(input("Enter the first num: "))
    num2 = float(input("Enter the second num: "))
    print(num1 / num2)