def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Cannot divide by zero!"

def calculator():
    while True:
        print("\n===== Simple Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("Select an option (1–5): ")

        if choice == '5':
            print("Thanks for using the calculator. See you again!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            print("❌ Invalid choice. Try again.")
            continue

        print(f"✅ Result: {result}")

if __name__ == "__main__":
    calculator()

