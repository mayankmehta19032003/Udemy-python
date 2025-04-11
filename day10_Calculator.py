import os


def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_accumulate = True
    first_number = float(input("What is the first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        next_number = float(input("What is the next number? "))

        result = operations[operation_symbol](first_number, next_number)
        print(f"{first_number} {operation_symbol} {next_number} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()


calculator()
    
