# Goal:
# Create a calculator program. It should:
# - print an introduction message
# - take input from the user
# - perform addition, subtraction, multiplication and division
# - print the calculation it performs AND the result

def _introduction(opeartion):
    welcome_string = "welcome to the calculator program."
    prompt_string = f"please give me two values to {opeartion}."
    print(f"{welcome_string}\n{prompt_string}")

def _get_number(index):
    number = float(input("number: "))
    return number


def _print_result(first_number, second_number, opeartion, result):
    print(f"{first_number}{opeartion}{second_number} = {result}")


#--------------------#

def add_numbers():
    _introduction("add")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 + num2
    _print_result(num1, num2, "+", result)

def multiply_numbers():
    _introduction("multiply")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 * num2
    _print_result(num1, num2, "*", result)


def divide_numbers():
    _introduction("divide")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 / num2
    _print_result(num1, num2, "/", result)


def subtract_numbers():
    _introduction("subtract")
    num1 = _get_number(1)
    num2 = _get_number(2)
    result = num1 - num2
    _print_result(num1, num2, "-", result)
