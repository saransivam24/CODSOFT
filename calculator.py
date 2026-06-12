def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation(+,-,*,/): ")

if operation == "+":
    result = add(num1, num2)
    print(result)
elif operation == "-":
    ans = sub(num1, num2)
    print(ans)
elif operation == "*":
    sol = product(num1, num2)
    print(sol)
elif operation == "/":
    value = division(num1, num2)
    print(value)
else:
    print("Invalid operation")
