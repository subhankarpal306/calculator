#python calculator

operator = input("Enter an operator (+, -, *, /):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result,2)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1}-{num2} = {round(result,2)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {round(result,2)} ")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1}/{num2} = {round(result,2)}")
    else:
        print("Error : Division by zero is not allowed.")
else:
    print("Invalid operator")