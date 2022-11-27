import math

# Request a float from the user, repeating the request if any ValueError occurs
def request_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError as error:
            print("The number was not in the correct format, please try again.")
            print(error)


# Request the operation from the user, repeating the request if the choice is not valid
def request_operation():
    while True:
        value = input("Please enter the operation (+, -, *, /): ")
        if value not in ["+", "-", "*", "/"]:
            print(f"'{value}' is not a supported operation, please try again.")
            continue
        return value


# Calculate the result of the specified operation on a pair of numbers.
def calculate(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        # Check if we can do the division without causing ZeroDivisonError.
        if number2 != 0:
            return number1 / number2
        else:
            return math.inf
    else:
        return None


def run_calculator():
    # Try to open the file that equations will be recorded in.
    # It is not fatal if the file cannot be opened, but inform the user that their history
    # will not be recorded.
    file = None
    try:
        file = open("history.txt", "a")
    except Exception as error:
        print(f"Error {error}")
        print(f"Your history will not be recorded for this session.")

    # Repeatedly ask for two numbers and an operation to perform on those numbers.
    while True:
        number1 = request_float("Please enter the first number : ")
        number2 = request_float("Please enter the second number: ")
        operation = request_operation()

        # Get the result of the user choice.
        result = calculate(number1, number2, operation)
        if result is None:
            print("The operation is not supported.")
            continue

        # Display the complete equation to the user.
        equation = f"{number1} {operation} {number2} = {result}"
        print(equation)
        print()

        # If the history file is available, record the equation.
        if file is not None:
            file.write(f"{equation}\n")

    if file is not None:
        file.close()


# Ask the user for a file to read the equations from
def display_equations_from_file():

    file_name = input("Please enter the file name: ")

    try:
        with open(file_name, "r") as file:
            print(f"Equations from '{file_name}':")
            for line in file.read().splitlines():
                print(line)
            print()
    except Exception as error:
        print("There was an error opening the file.")
        print(error)
            

while True:
    print("Please choose an option:")
    print("f - Display equations from a file.")
    print("c - Enter numbers into the calculator.")
    choice = input(": ").lower()
    if choice == "f":
        display_equations_from_file()
    elif choice == "c":
        run_calculator()
    else:
        print(f"'{choice}' is not valid, please try again.")
