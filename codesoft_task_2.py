#WAP to design a simple calculator with basic arithmetic operations. Prompt the user to input two numbers and
#an operation choice. Perform the calculation and display the result.
import math


def main():
    print("Scientific Calculator")
    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Trigonometric Functions")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            add()
        elif choice == '2':
            subtract()
        elif choice == '3':
            multiply()
        elif choice == '4':
            divide()
        elif choice == '5':
            exponentiation()
        elif choice == '6':
            square_root()
        elif choice == '7':
            trig_functions()
        elif choice == '8':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print("Result:", result)


def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print("Result:", result)


def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print("Result:", result)


def divide():
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    if num2 == 0:
        print("Error: Division by zero.")
    else:
        result = num1 / num2
        print("Result:", result)


def exponentiation():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    result = base ** exponent
    print("Result:", result)


def square_root():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Error: Cannot calculate square root of a negative number.")
    else:
        result = math.sqrt(num)
        print("Result:", result)


def trig_functions():
    print("\nTrigonometric Functions:")
    print("1. Sine")
    print("2. Cosine")
    print("3. Tangent")
    choice = input("Enter your choice (1/2/3): ")
    angle = float(input("Enter the angle in degrees: "))

    if choice == '1':
        result = math.sin(math.radians(angle))
    elif choice == '2':
        result = math.cos(math.radians(angle))
    elif choice == '3':
        result = math.tan(math.radians(angle))
    else:
        print("Invalid choice.")
        return

    print(f"Result: {result:.4f}")


if __name__ == "__main__":
    main()
