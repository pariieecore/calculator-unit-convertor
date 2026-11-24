# Menu Driven Calculator and Unit Converter

# Conversion factors
CONVERSIONS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


# Function to read valid numbers
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Arithmetic functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b


# Unit conversion function
def convert_units():
    print("\n--- Unit Conversion ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")

    choice = input("Enter your choice: ")

    if choice == "1":
        km = read_number("Enter kilometers: ")
        print("Miles:", km * CONVERSIONS["km_to_miles"])

    elif choice == "2":
        c = read_number("Enter Celsius: ")
        print("Fahrenheit:", (c * 9/5) + 32)

    elif choice == "3":
        kg = read_number("Enter kilograms: ")
        print("Pounds:", kg * CONVERSIONS["kg_to_pounds"])

    else:
        print("Invalid choice!")


# Main menu function
def main():
    while True:
        print("\n===== CALCULATOR MENU =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Unit Conversion")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")

            if choice == "1":
                print("Result:", add(a, b))

            elif choice == "2":
                print("Result:", subtract(a, b))

            elif choice == "3":
                print("Result:", multiply(a, b))

            elif choice == "4":
                print("Result:", divide(a, b))

        elif choice == "5":
            convert_units()

        elif choice == "6":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please try again.")


# Starting the program
if __name__ == "__main__":
    main()
