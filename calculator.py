# Calculator Class with Exception Handling

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."


calc = Calculator()

try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    print("\nChoose Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result =", calc.add(num1, num2))

    elif choice == 2:
        print("Result =", calc.subtract(num1, num2))

    elif choice == 3:
        print("Result =", calc.multiply(num1, num2))

    elif choice == 4:
        print("Result =", calc.divide(num1, num2))

    else:
        print("Invalid Choice.")

except ValueError:
    print("Error: Please enter valid numbers.")