


import math

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)

# Example usage:
try:
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print(f"The square root of {num} is {result}")
except ValueError as e:
    print(e)







def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if the choice is one of the four options
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        # Ask if the user wants another calculation
        next_calculation = input("Do you want to perform another calculation? (y/n): ")
        if next_calculation.lower() != 'y':
            break
    else:
        print("Invalid input")
