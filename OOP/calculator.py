class InvalidSignError(Exception):
    """Exception raised for invalid operation signs."""
    pass

def calculator(sign, a, b):
    # This checks if the sign is one of the specified characters
    if sign not in ["+", "-", "*", "/"]:
        raise InvalidSignError("Please use only the given signs: +, -, *, /.")
    # Perform calculation based on the sign
    if sign == '+':
        print('The sum is', a + b)
    elif sign == '-':
        print('The result is', a - b)
    elif sign == '*':
        print('Result is', a * b)
    elif sign == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        else:
            print('Result is', a / b)

try:
    sign = input("Please enter what you want to do (+, -, *, /): ")
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    calculator(sign, num1, num2)
except InvalidSignError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter valid numbers.")
