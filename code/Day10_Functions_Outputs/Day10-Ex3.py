# Calculator
from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    cont = True

    while cont:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if (
            input(
                f"Type 'y' to conitnue calculating with {answer} or type 'n' to exit: "
            )
            == "y"
        ):
            num1 = answer
        else:
            cont = False
            calculator()


calculator()
